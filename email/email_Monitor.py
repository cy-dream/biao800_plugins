import re
import time
import yaml
import poplib
import base64
import smtplib
import logging
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from email.mime.text import MIMEText

with open('email_conf.yml') as config:
    param = yaml.load(config)

logging.basicConfig(level=logging.INFO,
                    filename='email_Monitor.log',
                    datefmt='%Y-%m-%d %H:%M:%S', 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('Process Maintor')


def email_receive_login():
    try:
        pop3_server = param['receive_message']['receive_pop']
        server = poplib.POP3(pop3_server)
        #server.set_debuglevel(1)
        server.user(param['receive_message']['receive_account'])
        server.pass_(param['receive_message']['receive_password'])
        return server    
    except Exception as e:
        logger.error('def email_receive_login ERROR: ', exc_info=True)


def email_send_login():
    try:
        smtp_server = param['send_message']['send_smtp']
        server = smtplib.SMTP_SSL()
        server.connect(smtp_server, 587)
        #server.set_debuglevel(1)
        user = param['send_message']['send_account']
        passward = param['send_message']['send_password']
        server.login(user, passward)
        return server
    except Exception as e:
        logger.error('def email_send_login ERROR: ', exc_info=True)
        

def get_all_mails_and_id():
    mails_msg_list = []
    server = email_receive_login()
    logger.info(server.getwelcome().decode('utf-8'))
    logger.info('Message: %s, Size: %s' % server.stat())
    resp, mails, octets = server.list()
    for i in range(len(mails), 1, -1):
        lines= server.retr(i)[1]
        try:
            msg_content = b'\r\n'.join(lines).decode('utf-8')
        except Exception as e:
            pass
        msg = Parser().parsestr(msg_content)
        mails_msg_list.append({'msg':msg, '_id':i})
    server.quit()
    return mails_msg_list


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def judge(content_list):
    con_issue_list = list()
    try:
        for item in content_list:
            text = item['content_text'].replace('\n', '').replace('\r','')
            patt = r'运行情况如下：([\s\S]*);触发预警'
            con = re.search(patt,text, re.M|re.I)
            con = con.group(1)
            con = dict([item.split('：') for item in con.split(';')])
            num = set(con.values())
            #if len(num) == 1 and '0' in num:
            if len(num) < 5:
                logger.debug('run faild item:'+str(con))
                con_issue_list.append(item)
    except Exception as e:
        logger.error('Faild to judge result', exc_info=True)
        pass
    return con_issue_list


#parser email text
content_list = list()
def parser_info(msgs, indent=0):
    for item in msgs:
        msg = item['msg']
        _id = item['_id']
        content_dict = dict()
        if indent==0:
            #for header in ['From', 'To', 'Subject']:
            for header in ['From', 'Subject']:
                value = msg.get(header, '')
                if value:
                    if header=='Subject':
                        subject_value = decode_str(value)
                        content_dict['subject'] = subject_value
                    else:
                        hdr, addr = parseaddr(value)
                        name = decode_str(hdr)
                        value = u'%s <%s>' % (name, addr)
        if '运行结果预警' not in subject_value:
            continue
        try:
            content_type = msg.get_content_type()
            content = msg.get_payload()
            content_dict['_id'] = _id
            content_dict['content_text'] = base64.b64decode(content).decode()
            content_list.append(content_dict)
        except Exception as e:
            logger.error('Send print_info emails:', exc_info=True)
            pass
        break


def send_emails(emails):
    server = email_send_login()
    num = 0
    for email in emails:
        try:
            to = param['to_user']
            # MIMEText表示邮件发送具体内容
            content = MIMEText(email['content_text'])
            content['Subject'] = email['subject']
            content['From'] = param['send_message']['send_account']
            content['To']=','.join(to)
            server.sendmail(param['send_message']['send_account'],to,content.as_string())
            time.sleep(3)
            num += 1         
        except Exception as e:
            logger.error('Send Faild Emails:', exc_info=True)
            pass
    logger.info('def send_emails -- Email Success Nums: {}'.format(num))
    # close email box
    server.close()
 
        
def del_source_issume_email(con_issue_list):
    server = email_receive_login()
    try:
        num = 0
        for item in con_issue_list:
            server.dele(item['_id']) 
            num += 1     
    except Exception as e:
        logger.error('Send Faild emails:', exc_info=True)
        pass
    logger.info('def del_source_issume_email -- Delete Email Faild Nums: {}'.format(num))
    server.quit()


if __name__ == '__main__':
    msg = get_all_mails_and_id()
    parser_info(msg)
    logger.info('content_list NUMS: {}'.format(len(content_list)))
    con_issue_list = judge(content_list)
    logger.info('con_issue_list NUMS: {}'.format(len(con_issue_list)))
    if con_issue_list:
        send_emails(con_issue_list)
        del_source_issume_email(con_issue_list)
    logger.info('Finish -----------')