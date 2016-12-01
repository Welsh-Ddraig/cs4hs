from bottle import run, route, view, get, post, request
from itertools import count

###Class START WITH CAPITAL LETTERS

class Ticket:
    
    # _ signifies a private varaible. not to be used outside of this class.
    _ids = count (0)
    
    def __init__(self, image, name, email, date_of_birth, check_in): #not passing ID as we want it to create it.
        self.id = next(self._ids)
        self.mini_image = image
        self.name = name
        self.email = email
        self.dob = date_of_birth
        self.check_in = check_in

###Variables
    
PLACEHOLDER = "https://upload.wikimedia.org/wikipedia/commons/0/09/Man_Silhouette.png"
tickets = [
    Ticket(PLACEHOLDER,"Matt Evans", "mevans@stc.school.nz","27.01.1988", False),
    Ticket(PLACEHOLDER, "Superman", "superman@stc.school.nz", "15.12.1978", False),
    Ticket(PLACEHOLDER,"Batman", "batman@stc.school.nz", "23.07.1989",False),
    Ticket(PLACEHOLDER,"Hulk", "hulk@stc.school.nz", "26.06.2003",False)
    ]


###Pages


#index page
@route('/')
@view ('index')
def index():
    #need this function to attach the decarators above.
    pass


'''
Displays the check-in page. This also populates with the list of tickets.
and displays the result to the user
'''

#check-in page
@route('/check-in')
@view ('check-in')
def check_in():
    data = dict (ticket_list = tickets)
    return data

'''
displays the sell ticket page
'''
#sell ticket page
@route('/sell-ticket')
@view ('sell-ticket')
def sell_ticekt():
    pass


'''
Changes a ticket status to "checked-in"
and displays the result to the user
'''
@route('/check-in-success/<ticket_id>')
@view ('check-in-success')
def check_in_success(ticket_id):
    #need this function to attach the decarators above.
    ticket_id = int(ticket_id)
    found_ticket = None
    for ticket in tickets:
        if ticket.id == ticket_id:
            found_ticket = ticket
    data = dict (ticket = found_ticket) 
    found_ticket.check_in = True
    return data

'''
displays the sell ticket success page
'''
#sell ticket page
@route('/sell-ticket-success', method='POST')
@view ('sell-ticket-success')
def sell_ticekt_success():
    name = request.forms.get('name')
    email = request.forms.get('email')
    date_of_birth = request.forms.get('dob')
    
    new_ticket = Ticket(PLACEHOLDER, name, email, date_of_birth, False)
    tickets.append(new_ticket)



'''Allow the website to load CSS/Images fiales as long as they 
are stored in the css or images folders.
'''
@route('/css/:filename#,*#')
def send_static(filename):
    file = static_file(filename, root='./css/')
    return file


run(host='0.0.0.0', port = 8080, reloader=True, debug=True)