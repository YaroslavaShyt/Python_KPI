import re
import json
from datetime import datetime


DISCOUNT = {"RT": 1, "ST": 0.5, "AT": 0.6, "LT": 1.1}

TIC_DAY_LIM = {'LATE': {'LATE_MIN': 0, 'LATE_MAX': 10},
               'REG': {'REG_MIN': 11, 'REG_MAX': 60},
               'ADV': {'ADV_MIN': 61}}


class CustomerInfo:
    def __init__(self, name, surname, phone, email, is_student):
        self.customer_name = name
        self.customer_surname = surname
        self.customer_phone = phone
        self.customer_email = email
        self.customer_student = is_student

    @property
    def customer_student(self):
        return self.__customer_student

    @customer_student.setter
    def customer_student(self, is_student):
        if not isinstance(is_student, bool):
            raise TypeError('Incorrect type for student ticket existence! Use True or False.')
        self.__customer_student = is_student

    @property
    def customer_name(self):
        return self.__customer_name

    @customer_name.setter
    def customer_name(self, new_n):
        if not isinstance(new_n, str):
            raise TypeError('Incorrect type for name!')
        elif re.search('[^A-Za-z\'-]', new_n):
            raise ValueError('Incorrect character in name!')
        self.__customer_name = new_n

    @property
    def customer_surname(self):
        return self.__customer_surname

    @customer_surname.setter
    def customer_surname(self, new_s):
        if not isinstance(new_s, str):
            raise TypeError('Incorrect type for surname!')
        elif re.search('[^A-Za-z\'-]', new_s):
            raise ValueError('Incorrect character in surname!')
        self.__customer_surname = new_s

    @property
    def customer_phone(self):
        return self.__customer_phone

    @customer_phone.setter
    def customer_phone(self, new_ph):
        if not isinstance(new_ph, str):
            raise TypeError('Incorrect type for phone number!')
        elif re.search('[^+0-9]', new_ph):
            raise ValueError('Incorrect character in phone number!')
        self.__customer_phone = new_ph

    @property
    def customer_email(self):
        return self.__customer_email

    @customer_email.setter
    def customer_email(self, new_e):
        if not isinstance(new_e, str):
            raise TypeError("Incorrect type for email!")
        elif not re.search(r'[\S+@a-z.a-z]', new_e):
            raise ValueError("Invalid email!")
        self.__customer_email = new_e

    def __str__(self):
        return f'Name: {self.customer_name}\n' \
               f'Surname: {self.customer_surname}\n' \
               f'Phone number: {self.customer_phone}\n' \
               f'Email: {self.customer_email}'


class Event:
    def __init__(self, id_event):
        with open('eventsinfo.json', 'r') as f:
            self.data = json.load(f)
        self.id_event = id_event
        self.event_name = self.data["events"][self.id_event]["name"]
        self.specialization = self.data["events"][self.id_event]["specialization"]
        self.ticket_price = self.data["events"][self.id_event]["price"]
        self.event_date = self.data["events"][self.id_event]["date"]
        self.event_time = self.data["events"][self.id_event]["time"]

    @property
    def id_event(self):
        return self.__id_event

    @id_event.setter
    def id_event(self, new_id):
        if not isinstance(new_id, str):
            raise TypeError('Incorrect type for event id!')
        elif new_id not in self.data["events"]:
            raise ValueError('This event does not exist!')
        self.__id_event = new_id

    @property
    def event_name(self):
        return self.__event_name

    @event_name.setter
    def event_name(self, new_n):
        if not isinstance(new_n, str):
            raise TypeError('Incorrect type for event name!')
        self.__event_name = new_n

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, new_s):
        if not isinstance(new_s, str):
            raise TypeError('Incorrect type for specialization!')
        elif re.search(r'[^A-Za-z\s,\']', new_s):
            raise ValueError('Incorrect symbol in specializations!')
        self.__specialization = new_s

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, new_p):
        if not isinstance(new_p, int | float):
            raise TypeError('Incorrect type for price!')
        if new_p < 0:
            raise ValueError('Price cannot be less 0')
        self.__ticket_price = new_p

    @property
    def event_date(self):
        return self.__event_date

    @event_date.setter
    def event_date(self, new_d):
        if not isinstance(new_d, str):
            raise TypeError('Incorrect type for date!')
        elif re.search(r'[^0-9.\s]', new_d):
            raise ValueError('Incorrect chars in date!')
        self.__event_date = new_d

    @property
    def event_time(self):
        return self.__event_time

    @event_time.setter
    def event_time(self, new_t):
        if not isinstance(new_t, str):
            raise TypeError('Incorrect type for event time!')
        elif re.search('r[^0-9:]', new_t):
            raise ValueError('Incorrect chars in event time!')
        self.__event_time = new_t

    def __str__(self):
        return f'Event: {self.event_name}\n' \
               f'Spec.: {self.specialization}\n' \
               f'Price without discount: {self.ticket_price}\n' \
               f'Date: {self.event_date}\n' \
               f'Time: {self.event_time}'


class RegularTicket:
    def __init__(self, event, customer, num, unique='RT'):
        self.event = event
        self.customer = customer
        self.ticket_num = num
        self.unique_id = unique
        self.discount = DISCOUNT[self.unique_id]
        self.unique_cod = self.event.id_event + self.unique_id + str(self.ticket_num)
        self.ticket_price = self.event.ticket_price
        self.write_to_report()

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, new_p):
        if not isinstance(new_p, int | float):
            raise TypeError('Incorrect type for price!')
        elif new_p < 0:
            raise ValueError('Price cannot be less 0')
        self.__ticket_price = round(new_p * self.discount, 2)

    @property
    def ticket_num(self):
        return self.__ticket_num

    @ticket_num.setter
    def ticket_num(self, new_n):
        if not isinstance(new_n, int):
            raise TypeError('Incorrect type for ticket number!')
        elif new_n < 1:
            raise ValueError('Incorrect value for ticket number!')
        self.__ticket_num = new_n

    @property
    def unique_id(self):
        return self.__unique_id

    @unique_id.setter
    def unique_id(self, new_id):
        with open('eventsinfo.json', 'r') as e:
            data = json.load(e)
        if not isinstance(new_id, str):
            raise TypeError('Incorrect type for unique id!')
        elif new_id not in data["ticket-types"]:
            raise KeyError('Unique id does not exist!')
        self.__unique_id = new_id

    def write_to_report(self):
        with open('ordersreport.json', 'r') as o:
            data = json.load(o)
            data["ticket"][self.unique_cod] = {}
            data["ticket"][self.unique_cod]["name"] = self.event.event_name
            data["ticket"][self.unique_cod]["price"] = self.ticket_price
            data["ticket"][self.unique_cod]["date"] = self.event.event_date
            data["ticket"][self.unique_cod]["time"] = self.event.event_time
            data["ticket"][self.unique_cod]["customer"] = self.customer.__str__()
        with open('ordersreport.json', 'w') as o:
            json.dump(data, o, indent=4)

    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, new_e):
        if not isinstance(new_e, object):
            raise TypeError('Incorrect type for event!')
        self.__event = new_e

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, new_c):
        if not isinstance(new_c, object):
            raise TypeError('Incorrect type for customer!')
        self.__customer = new_c

    def __str__(self):
        return f'-------TICKET № {self.unique_cod}----------\n' \
               f'{self.event}\n' \
               f'Total price: {self.ticket_price}\n' \
               f'-------CUSTOMER----------------\n' \
               f'Customer:\n {self.customer}' \



class StudentTicket(RegularTicket):
    def __init__(self, event, customer, num, unique='ST'):
        super().__init__(event, customer, num, unique)


class AdvancedTicket(RegularTicket):
    def __init__(self, event, customer, num, unique='AT'):
        super().__init__(event, customer, num, unique)


class LateTicket(RegularTicket):
    def __init__(self, event, customer, num, unique='LT'):
        super().__init__(event, customer, num, unique)


class MakeOrder:
    def __init__(self, customer):
        with open('eventsinfo.json', 'r') as f:
            self.data = json.load(f)
        with open('orders.json', 'r') as o:
            self.orders = json.load(o)
        self.customer = customer
        self.order_date = f'{datetime.now():%d.%m.%Y}'
        self.ticket_types = [RegularTicket, StudentTicket, AdvancedTicket, LateTicket]
        self.order_list = []
        self.tickets_list = []

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, new_c):
        if not isinstance(new_c, object):
            raise TypeError('Incorrect data for customer!')
        self.__customer = new_c

    def print_events(self):
        for i in self.data['events']:
            print(f"(ID-{i})  {self.data['events'][str(i)]['name']}\n"
                  f"spec.:   {self.data['events'][str(i)]['specialization']}\n"
                  f"price:   {self.data['events'][str(i)]['price']}\n"
                  f"time:    {self.data['events'][str(i)]['time']}\n"
                  f"date:    {self.data['events'][str(i)]['date']}\n")

    def buy_tickets(self):
        while True:
            id_event = input('Enter id of chosen event or quit(0): ')
            if int(id_event) == 0:
                break
            elif id_event not in self.data["events"]:
                print('Event does not exist!')
            elif not self.orders["all-left"][id_event]:
                print('Sold out!')
            elif not self.count_day_dif(id_event):
                print('Event has ended!')
            else:
                self.order_list.append(str(id_event))

    def form_order(self):
        for i in self.order_list:
            ticket = self.define_ticket_type(i)
            self.tickets_list.append(self.return_ticket(ticket, i))
            self.orders["all-sold"][i] += 1
            self.orders["all-left"][i] -= 1
        with open('orders.json', 'w') as f:
            json.dump(self.orders, f, indent=3)

    def define_ticket_type(self, i):
        type_tick = RegularTicket
        if self.customer.customer_student:
            type_tick = StudentTicket
        else:
            dif = self.count_day_dif(i)
            if dif in range(TIC_DAY_LIM['LATE']['LATE_MIN'], TIC_DAY_LIM['LATE']['LATE_MAX']+1):
                type_tick = LateTicket
            elif dif >= TIC_DAY_LIM['ADV']['ADV_MIN']:
                type_tick = AdvancedTicket
        return type_tick

    def return_ticket(self, type_tick, ev):
        if type_tick in self.ticket_types:
            return type_tick(Event(ev), self.customer, self.orders["all-sold"][ev]+1)
        raise ValueError('No tickets of such type available!')

    def count_day_dif(self, id_event):
        return (datetime.strptime(str(self.data["events"][id_event]["date"]), '%d.%m.%Y') -
                datetime.strptime(self.order_date, '%d.%m.%Y')).days

    def show_info(self):
        for i in self.tickets_list:
            print(i)

    def count_total(self):
        return f'TOTAL TO PAY: {sum([i.ticket_price for i in self.tickets_list])}'

    @staticmethod
    def search_tickets():
        id = input('Enter your ticket code: ')
        with open('ordersreport.json', 'r') as f:
            orders = json.load(f)
        for i in orders["ticket"]:
            if i == id:
                return f'Ticket found:\n\n' \
                       f'-----------------------------------\n' \
                       f'NUMBER: {i}\n' \
                       f'name: {orders["ticket"][i]["name"]}\n' \
                       f'price: {orders["ticket"][i]["price"]}\n' \
                       f'date: {orders["ticket"][i]["date"]}\n' \
                       f'time: {orders["ticket"][i]["time"]}\n\n' \
                       f'customer:\n{orders["ticket"][i]["customer"]}\n' \
                       f'-----------------------------------'
        return f'Ticket does not exist.'


try:
    c = CustomerInfo('Petro', 'Petrenko', '098765432', 'petpet@gmail.com', False)
    m = MakeOrder(c)
    m.print_events()
    m.buy_tickets()
    m.form_order()
    m.show_info()
    print(m.count_total())
    print(m.search_tickets())
except Exception as ex:
    print(ex)
