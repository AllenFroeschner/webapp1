# A simple script to calculate BMI
from pywebio.input import *
from pywebio import *
from pywebio.output import *
from datetime import date, datetime, timedelta

class Person:
    file = "./USERS/Angel_B.txt"
    name = "Angel B"
    isAdmin = False
    mondayStart = "OFF"
    mondayEnd = "OFF"
    tusStart = "OFF"
    tusEnd = "OFF"
    wedStart = "OFF"
    wedEnd = "00:00"
    thuStart = "16:00"
    thuEnd = "00:00"
    friStart = "17:00"
    friEnd = "01:00"
    satStart = "16:00"
    satEnd = "01:00"
    sunStart = "13:00"
    sunEnd = "21:00"
    NmondayStart = "OFF"
    NmondayEnd = "OFF"
    NtusStart = "OFF"
    NtusEnd = "OFF"
    NwedStart = "OFF"
    NwedEnd = "00:00"
    NthuStart = "16:00"
    NthuEnd = "00:00"
    NfriStart = "17:00"
    NfriEnd = "01:00"
    NsatStart = "16:00"
    NsatEnd = "01:00"
    NsunStart = "13:00"
    NsunEnd = "21:00"

    def setTimes(self,lines=[""]):
        self.mondayStart = lines[0]
        self.mondayEnd = lines[1]
        self.tusStart = lines[2]
        self.tusEnd = lines[3]
        self.wedStart = lines[4]
        self.wedEnd = lines[5]
        self.thuStart = lines[6]
        self.thuEnd = lines[7]
        self.friStart = lines[8]
        self.friEnd = lines[9]
        self.satStart = lines[10]
        self.satEnd = lines[11]
        self.sunStart = lines[12]
        self.sunEnd = lines[13]
        self.NmondayStart = lines[15]
        self.NmondayEnd = lines[16]
        self.NtusStart = lines[17]
        self.NtusEnd = lines[18]
        self.NwedStart = lines[19]
        self.NwedEnd = lines[20]
        self.NthuStart = lines[21]
        self.NthuEnd = lines[22]
        self.NfriStart = lines[23]
        self.NfriEnd = lines[24]
        self.NsatStart = lines[25]
        self.NsatEnd = lines[26]
        self.NsunStart = lines[27]
        self.NsunEnd = lines[28]
    def setName(self, x=str("")):
        self.name=x
    def getName(self):
        return self.name
    def setAdmin(self, x=bool(False)):
        self.isAdmin=x
    def setFile(self,x=str("")):
        self.file=x

def read_data(user= Person(),name=""):
    lines = []
    with open(name) as f:
        lines = f.readlines()

    user.setTimes(lines)


def user():
    set_env(title='Awesome PyWebIO!!')
    names = []
    Angel_B = Person()

    Audrey_C = Person()
    Audrey_C.setName("Audrey C")
    Audrey_C.setFile("./USERS/Audrey_C.txt")

    Berenice_P = Person()
    Berenice_P.setName("Berenice P")
    Berenice_P.setFile("./USERS/Berenice_P.txt")

    Flora_V = Person()
    Flora_V.setName("Flora V")
    Flora_V.setFile("./USERS/Flora_V.txt")

    Ivorie_C= Person()
    Ivorie_C.setName("Ivorie C")
    Ivorie_C.setFile("./USERS/Ivorie_C.txt")
    Ivorie_C.setAdmin(True)

    Leticia_C = Person()
    Leticia_C.setName("Leticia C")
    Leticia_C.setFile("./USERS/Leticia_C.txt")


    names.append(Angel_B)
    names.append(Audrey_C)
    names.append(Berenice_P)
    names.append(Flora_V)
    names.append(Ivorie_C)
    names.append(Leticia_C)
    for name in names:
        read_data(name,name.file)


    popup('select option',[put_button("Employee Login",onclick=close_popup)])

    fname = input.input("Input your first name and last initial：",placeholder="please enter your name", type="text")


    for name in names:

        if fname == name.getName():
            #put_text([name.name , "Monday: "+ name.mondayStart+"-"+ name.mondayEnd])
            set_schedule(name)
            if name.isAdmin==True:
                put_text('hi')
                passwd= input.input("Input password:", type='text')
                pas="ABC123"
                if(passwd==pas):
                    output.put_button('Set Schedule',onclick=set_schedule())

            put_row([
                put_column([
                    put_text(name.name),
                    put_row([
                        put_text('Monday: '),
                        put_text('start: '+name.mondayStart),
                        put_text('end: '+name.mondayEnd),
                    ]),put_row([
                        put_text('Tuesday: '),
                        put_text('start: '+name.tusStart),
                        put_text('end: '+name.tusEnd),
                    ]),put_row([
                        put_text('Wednesday: '),
                        put_text('start: '+name.wedStart),
                        put_text('end: '+name.wedEnd),
                    ]),put_row([
                        put_text('Thursday: '),
                        put_text('start: '+name.thuStart),
                        put_text('end: '+name.thuEnd),
                    ]),put_row([
                        put_text('Friday: '),
                        put_text('start: '+name.friStart),
                        put_text('end: '+name.friEnd),
                    ]),put_row([
                        put_text('Saturday: '),
                        put_text('start: '+name.satStart),
                        put_text('end: '+name.satEnd),
                    ]),put_row([
                        put_text('sunday: '),
                        put_text('start: '+name.sunStart),
                        put_text('end: '+name.sunEnd),
                    ]),





                ]),

            ])
def nxtWeek(name= Person()):
    put_row([
        put_column([
            put_text(name.name),
            put_row([
                put_text('Monday: '),
                put_text('start: ' + name.NmondayStart),
                put_text('end: ' + name.NmondayEnd),
            ]), put_row([
                put_text('Tuesday: '),
                put_text('start: ' + name.NtusStart),
                put_text('end: ' + name.NtusEnd),
            ]), put_row([
                put_text('Wednesday: '),
                put_text('start: ' + name.NwedStart),
                put_text('end: ' + name.NwedEnd),
            ]), put_row([
                put_text('Thursday: '),
                put_text('start: ' + name.NthuStart),
                put_text('end: ' + name.NthuEnd),
            ]), put_row([
                put_text('Friday: '),
                put_text('start: ' + name.NfriStart),
                put_text('end: ' + name.NfriEnd),
            ]), put_row([
                put_text('Saturday: '),
                put_text('start: ' + name.NsatStart),
                put_text('end: ' + name.NsatEnd),
            ]), put_row([
                put_text('sunday: '),
                put_text('start: ' + name.NsunStart),
                put_text('end: ' + name.NsunEnd),
            ]), put_row([ put_text('This Week: 11/Jul/2022 17/Jul/2022')])

        ]),

    ])

def set_schedule(name = Person()):
    def select_date(set_value):
        day = date.today()

        #dt = datetime.strptime(day, '%d/%b/%Y')

        start = day - timedelta(days=day.weekday())
        end = start + timedelta(days=6)
        start1 = start + timedelta(days=7)
        end1 = start1 + timedelta(days=6)
        with popup('Select Date range'):
            put_buttons([start.strftime('%d/%b/%Y')+' '+end.strftime('%d/%b/%Y')], onclick=[lambda: set_value(start.strftime('%d/%b/%Y')+' '+end.strftime('%d/%b/%Y'), 'This Week')])
            put_buttons([start1.strftime('%d/%b/%Y')+' '+end1.strftime('%d/%b/%Y')], onclick=[lambda: set_value(start1.strftime('%d/%b/%Y')+' '+end1.strftime('%d/%b/%Y'), 'Next Week'),close_popup()])
        return start1.strftime('%d/%b/%Y')+' '+end1.strftime('%d/%b/%Y')
    d = input.input('Date', action=('Select', select_date), readonly=True)
    put_text(d)
    if d == '18/Jul/2022 24/Jul/2022':
        nxtWeek(name)



if __name__ == '__main__':
    #user()
    import argparse
    from pywebio.platform.tornado_http import start_server as start_http_server
    from pywebio import start_server as start_ws_server

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    parser.add_argument("--http", action="store_true", default=False, help='Whether to enable http protocol for communicates')
    args = parser.parse_args()

    if args.http:
        start_http_server(user, port=args.port)
    else:
        # Since some cloud server may close idle connections (such as heroku),
        # use `websocket_ping_interval` to  keep the connection alive
        start_ws_server(user, port=args.port, websocket_ping_interval=30)
