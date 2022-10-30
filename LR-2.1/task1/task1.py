import re
import json
from datetime import datetime


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
        if re.search('[^A-Za-z\'-]', new_n):
            raise ValueError('Incorrect character in name!')
        self.__customer_name = new_n

    @property
    def customer_surname(self):
        return self.__customer_surname

    @customer_surname.setter
    def customer_surname(self, new_s):
        if not isinstance(new_s, str):
            raise TypeError('Incorrect type for surname!')
        if re.search('[^A-Za-z\'-]', new_s):
            raise ValueError('Incorrect character in surname!')
        self.__customer_surname = new_s

    @property
    def customer_phone(self):
        return self.__customer_phone

    @customer_phone.setter
    def customer_phone(self, new_ph):
        if not isinstance(new_ph, str):
            raise TypeError('Incorrect type for phone number!')
        if re.search('[^+0-9]', new_ph):
            raise ValueError('Incorrect character for phone number!')
        self.__customer_phone = new_ph

    @property
    def customer_email(self):
        return self.__customer_email

    @customer_email.setter
    def customer_email(self, new_e):
        if not isinstance(new_e, str):
            raise TypeError("Incorrect type for email!")
        if not re.search(r'[\S+@a-z.a-z]', new_e):
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
        if new_id not in self.data["events"]:
            raise ValueError('This event does not exist!')
        self.__id_event = new_id

    @property
    def event_name(self):
        return self.__event_name

    @event_name.setter
    def event_name(self, new_n):
        if not isinstance(new_n, str):
            raise TypeError('Incorrect type for event name')
        self.__event_name = new_n

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, new_s):
        if not isinstance(new_s, str | list):
            raise TypeError('Incorrect type for specialization!')
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
            raise TypeError('Incorrect type for date and time!')
        if re.search(r'[^0-9.:\s]', new_d):
            raise ValueError('Incorrect chars in date or time!')
        self.__event_date = new_d

    @property
    def event_time(self):
        return self.__event_time

    @event_time.setter
    def event_time(self, new_t):
        if not isinstance(new_t, str):
            raise TypeError('Incorrect type for event time!')
        if re.search('r[^0-9:]', new_t):
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
        self.unique_cod = self.event.id_event + self.unique_id + str(self.ticket_num)
        print(self.unique_id)
        self.ticket_price = self.event.ticket_price
        self.write_to_report()

    def write_to_report(self):
        with open('ordersreport.json', 'r') as f:
            k = json.load(f)
            k["ticket"][self.unique_cod] = {}
            k["ticket"][self.unique_cod]["name"] = self.event.event_name
            k["ticket"][self.unique_cod]["price"] = self.ticket_price
            k["ticket"][self.unique_cod]["date"] = self.event.event_date
            k["ticket"][self.unique_cod]["time"] = self.event.event_time
            k["ticket"][self.unique_cod]["customer"] = self.customer.__str__()
        with open('ordersreport.json', 'w') as f:
            json.dump(k, f, indent=4)

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
    def __init__(self, event, customer, num, unique='ST', discount=0.5):
        self.discount = discount
        super().__init__(event, customer, num, unique)

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, new_p):
        if not isinstance(new_p, int | float):
            raise TypeError('Incorrect type for price!')
        if new_p < 0:
            raise ValueError('Price cannot be less 0')
        self.__ticket_price = round(new_p * self.discount, 2)


class AdvancedTicket(RegularTicket):
    def __init__(self, event, customer, num, unique='AT', discount=0.6):
        self.discount = discount
        super().__init__(event, customer, num, unique)

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, new_p):
        if not isinstance(new_p, int | float):
            raise TypeError('Incorrect type for price!')
        if new_p < 0:
            raise ValueError('Price cannot be less 0')
        self.__ticket_price = round(new_p * self.discount, 2)


class LateTicket(RegularTicket):
    def __init__(self, event, customer, num, unique='LT', discount=1.1):
        self.discount = discount
        super().__init__(event, customer, num, unique)

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, new_p):
        if not isinstance(new_p, int | float):
            raise TypeError('Incorrect type for price!')
        if new_p < 0:
            raise ValueError('Price cannot be less 0')
        self.__ticket_price = round(new_p * self.discount, 2)


class MakeOrder:
    def __init__(self, customer):
        self.customer = customer
        self.order_date = f'{datetime.now():%d.%m.%Y}'
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

    @staticmethod
    def print_events():
        with open('eventsinfo.json', 'r') as f:
            data = json.load(f)
        for i in data['events']:
            print(f"(ID-{i})  {data['events'][str(i)]['name']}\n"
                  f"spec.:   {data['events'][str(i)]['specialization']}\n"
                  f"price:   {data['events'][str(i)]['price']}\n"
                  f"time:    {data['events'][str(i)]['time']}\n"
                  f"date:    {data['events'][str(i)]['date']}\n")

    def buy_tickets(self):
        with open('eventsinfo.json', 'r') as f:
            data = json.load(f)
        choice = 1,
        while choice:
            condition = 1
            while condition:
                id = int(input('Enter id of chosen event: '))
                if str(id) in data["events"]:
                    condition = 0
                else:
                    print('Event does not exist!')
            self.order_list.append(str(id))
            condition = 1
            while condition:
                choice = int(input('Add more/quit? - 1/0: '))
                if not isinstance(choice, int) or choice < 0 or choice > 1:
                    print('Incorrect user input for choice!')
                else:
                    condition = 0

    def define_ticket_type(self):
        with open('orders.json', 'r') as o:
            orders = json.load(o)
        if self.customer.customer_student:
            for i in self.order_list:
                if not orders["all-left"][i]:
                    print('Event id: ', i, '. All the tickets have been sold! :(')
                else:
                    self.tickets_list.append(StudentTicket(Event(i), self.customer, orders["all-sold"][i]+1))
        else:
            for i in self.order_list:
                if not orders["all-left"][i]:
                    print('Event id: ', i, '. All the tickets have been sold! :(')
                else:
                    dif = self.count_day_dif(i)
                    if dif < 0:
                        print('Event has been finished!')
                    elif 0 < dif < 10:
                        self.tickets_list.append(LateTicket(Event(i), self.customer, orders["all-sold"][i]+1))
                    elif 10 <= dif < 60:
                        self.tickets_list.append(RegularTicket(Event(i), self.customer, orders["all-sold"][i]+1))
                    elif dif > 60:
                        self.tickets_list.append(AdvancedTicket(Event(i), self.customer, orders["all-sold"][i]+1))
                    orders["all-sold"][i] += 1
                    orders["all-left"][i] -= 1
        with open('orders.json', 'w') as f:
            json.dump(orders, f, indent=3)

    def count_day_dif(self, id_event):
        with open('eventsinfo.json', 'r') as e:
            events_info = json.load(e)
        date = str(events_info["events"][id_event]["date"])
        return (datetime.strptime(date, '%d.%m.%Y') - datetime.strptime(self.order_date, '%d.%m.%Y')).days

    def show_info(self):
        for i in self.tickets_list:
            print(i)

    def count_total(self):
        total = 0
        self.show_info()
        for i in self.tickets_list:
            total += i.ticket_price
        print(f'TOTAL TO PAY: {total}')

    @staticmethod
    def search_tickets():
        id = input('Enter your ticket code: ')
        with open('ordersreport.json', 'r') as f:
            k = json.load(f)
        for i in k["ticket"]:
            if i == id:
                return f'Ticket found:\n' \
                       f'name: {k["ticket"][i]["name"]}\n' \
                       f'price: {k["ticket"][i]["price"]}\n' \
                       f'date: {k["ticket"][i]["date"]}\n' \
                       f'time: {k["ticket"][i]["time"]}\n' \
                       f'customer:\n    {k["ticket"][i]["customer"]}'
        return f'Ticket does not exist.'


c = CustomerInfo('Petro', 'Petrenko', '098765432', 'petpet@gmail.com', True)
m = MakeOrder(c)
m.print_events()
m.buy_tickets()
m.define_ticket_type()
m.count_total()
print(m.search_tickets())
