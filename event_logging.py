import win32evtlog
import win32evtlogutil

class WriteEvent: 
    def __init__(self, log_name, source_name):
        self.log_name = log_name
        self.source_name = source_name

    def log_event(self, event_type, message, event_id):
        if event_type.lower() == 'information':
            event_type_id = win32evtlog.EVENTLOG_INFORMATION_TYPE
            print('information')
        elif event_type.lower() == 'warning':
            event_type_id = win32evtlog.EVENTLOG_WARNING_TYPE
            print('warning')
        elif event_type.lower() == 'error':
            event_type_id = win32evtlog.EVENTLOG_ERROR_TYPE
            print('error')
        else:
            raise ValueError("Invalid event type")

        win32evtlogutil.ReportEvent(self.log_name,
                                    eventType=event_type_id,
                                    eventID=event_id,
                                    strings=[message])

'''

win32evtlogutil.ReportEvent(ApplicationName, EventID, EventCategory,EventType,Inserts, Data, SID)

'''

'''
logger = WriteEvent(log_name='MicrotechSystemsInc', source_name='MicrotechSystemsInc')
logger.log_event('information', 'Application started', 1001)
logger.log_event('error', 'An error occurred in module X', 1002)
'''