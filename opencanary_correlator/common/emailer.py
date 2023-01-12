import smtplib
import mandrill
import opencanary_correlator.common.config as c
from email.mime.text import MIMEText
from opencanary_correlator.common.logs import logger

def send_email(from_='notifications@opencanary.org', to='', subject='', message='', server='', port=25):
    logger.debug('Emailing {}'.format(to))  # Added .format() method for string formatting
    if not server:
        return

    msg = MIMEText(message)

    msg['Subject'] = subject
    msg['From'] = from_
    msg['To'] = to

    s = smtplib.SMTP(server, port)
    try:
        s.sendmail(from_, [to], msg.as_string())
        logger.info('Email sent to {}'.format(to))  # Added .format() method for string formatting
    except Exception as e:  # Replaced Exception, e with Exception as e
        logger.error('Email sending produced exception {}'.format(e))  # Added .format() method for string formatting
    s.quit()

def mandrill_send(to=None, subject=None, message=None, reply_to=None):
    try:
        mandrill_client = mandrill.Mandrill(c.config.getVal("console.mandrill_key"))
        message = {
         'auto_html': None,
         'auto_text': None,
         'from_email': 'notifications@opencanary.org',
         'from_name': 'OpenCanary',
         'text': message,
         'subject': subject,
         'to': [{'email': to,
                 'type': 'to'}],
        }
        if reply_to:
            message["headers"] = { "Reply-To": reply_to }

        result = mandrill_client.messages.send(message=message, asynchronous=False, ip_pool='Main Pool')


    except mandrill.Error as e:  # Replaced mandrill.Error, e with mandrill.Error as e
        print('A mandrill error occurred: {} - {}'.format(e.__class__, e))  # Added .format() method for string formatting
