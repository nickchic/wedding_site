from django.shortcuts import render, redirect
from .models import Guest, Invite

def index(request):
    return render(request, 'form/index.html')

def guest_form_zero(request):
    print(request.POST)
    invite = Invite.objects.get(id=request.POST['id'])

    if request.POST['attending_one'] == 'yes':
         invite.guest_1.attending = True

    if request.POST['attending_two'] == 'yes':
         invite.guest_2.attending = True

    invite.completed = True
    invite.guest_1.rsvp = True
    invite.guest_2.rsvp = True
    invite.guest_1.save()
    invite.guest_2.save()
    invite.save()
    return redirect('/')

def guest_form_one(request):
    print(request.POST)
    invite = Invite.objects.get(id=request.POST['id'])

    if request.POST['attending_one'] == 'yes':
         invite.guest_1.attending = True

    if request.POST['attending_two'] == 'yes':
         invite.guest_2.attending = True

    if request.POST['staying_one'] == 'yes':
        invite.guest_1.staying = True

    if request.POST['staying_two'] == 'yes':
        invite.guest_2.staying = True

    if request.POST['rehearsal_one'] == 'yes':
        invite.guest_1.rehearsal = True

    if request.POST['rehearsal_two'] == 'yes':
        invite.guest_2.rehearsal = True

    if request.POST['color_one'] == 'yes':
        invite.guest_1.color_war = True

    if request.POST['color_two'] == 'yes':
        invite.guest_2.color_war = True

    invite.guest_1.shirt_size = request.POST['shirt_one']
    invite.guest_2.shirt_size = request.POST['shirt_two']

    invite.completed = True
    invite.guest_1.rsvp = True
    invite.guest_2.rsvp = True
    invite.guest_1.save()
    invite.guest_2.save()
    invite.save()
    return redirect('/')

def guest_form_two(request):
    print(request.POST)
    invite = Invite.objects.get(id=request.POST['id'])

    if request.POST['attending_one'] == 'yes':
         invite.guest_1.attending = True

    staying = False
    if request.POST['staying'] == 'yes':
        invite.guest_1.staying = True

    if request.POST['rehearsal_one'] == 'yes':
        invite.guest_1.rehearsal = True

    if request.POST['color_one'] == 'yes':
        invite.guest_1.color_war = True

    if request.POST['plus_one'] == 'yes':
        Guest.objects.create(first_name = request.POST['guest_first'], last_name = request.POST['guest_last'], attending=True, staying=request.POST['staying_two'], rsvp=True, shirt_size = request.POST['shirt_two'], rehearsal=request.POST['rehearsal_two'], color_war=request.POST['color_two']);

    invite.guest_1.shirt_size = request.POST['shirt_one']

    invite.completed = True
    invite.guest_1.rsvp = True
    invite.guest_1.save()
    invite.save()
    return redirect('/')

def guest_form_three(request):
    print(request.POST)
    invite = Invite.objects.get(id=request.POST['id'])

    if request.POST['attending_one'] == 'yes':
         invite.guest_1.attending = True

    invite.completed = True
    invite.guest_1.rsvp = True
    invite.guest_1.save()
    invite.save()
    return redirect('/')

def guest_form_four(request):
    print(request.POST)
    invite = Invite.objects.get(id=request.POST['id'])

    if request.POST['attending_one'] == 'yes':
         invite.guest_1.attending = True

    if request.POST['plus_one'] == 'yes':
        Guest.objects.create(first_name = request.POST['guest_first'], last_name = request.POST['guest_last'], attending=True, staying=request.POST['staying_two'], rsvp=True);

    invite.completed = True
    invite.guest_1.rsvp = True
    invite.guest_1.save()
    invite.save()
    return redirect('/')

def guest_view(request):

    all_guests = Guest.objects.all()
    attending_total = 0;
    staying_total = 0;
    rehearsal_total = 0;
    color_total = 0;
    rsvp_total = 0;
    shirts = {
        's':0,
        'm':0,
        'l':0,
        'xl':0,
        'xxl':0,
    }
    for guest in all_guests:
        if guest.attending:
            attending_total += 1
        if guest.staying:
            staying_total += 1
        if guest.rehearsal:
            rehearsal_total += 1
        if guest.color_war:
            color_total += 1
        if guest.rsvp:
            rsvp_total += 1

        if guest.shirt_size == 'S':
            shirts['s'] += 1
        elif guest.shirt_size == 'M':
            shirts['m'] += 1
        elif guest.shirt_size == 'L':
            shirts['l'] += 1
        elif guest.shirt_size == 'XL':
            shirts['xl'] += 1
        elif guest.shirt_size == 'XXL':
            shirts['xxl'] += 1



    all_invites = Invite.objects.all()
    opened_invites = 0
    completed_invites = 0
    for invite in all_invites:
        if invite.opened:
            opened_invites += 1
        if invite.completed:
            completed_invites += 1

    context = {
        'guests': all_guests,
        'total':attending_total,
        'stay':staying_total,
        'rsvp':rsvp_total,
        'rehearsal':rehearsal_total,
        'shirts':shirts,
        'invites':all_invites,
        'open':opened_invites,
        'completed':completed_invites,
    }
    return render(request, 'form/all_guests.html', context)

def passcode(request):
    invite = Invite.objects.get(passcode=request.POST['passcode'])
    print(invite.guest_1.first_name)
    print(invite.guest_2.first_name)
    print(invite.form_type)
    return redirect('/')

def form(request):
    passcode = request.POST['passcode']
    passcode = passcode.upper()

    try:
        invite = Invite.objects.get(passcode=passcode)
    except:
        return render(request, 'form/error.html')

    context = {
        'invite': invite
    }

    if invite.completed:
        return render(request, 'form/already_complete.html', context)

    invite.opened = True;
    invite.save()
    if invite.form_type == 0:
        return render(request, 'form/form_0.html', context)
    elif invite.form_type == 1:
        return render(request, 'form/form_1.html', context)
    elif invite.form_type == 2:
        return render(request, 'form/form_2.html', context)
    elif invite.form_type == 3:
        return render(request, 'form/form_3.html', context)
    else:
        return render(request, 'form/form_4.html', context)

def edit_guest(request, guest_id):
    guest = Guest.objects.get(id=guest_id)

    guest.first_name = request.POST['first_name']
    guest.last_name = request.POST['last_name']
    
    if request.POST['attending'] == 'yes':
        guest.attending = True
    else:
        guest.attending = False

    if request.POST['staying'] == 'yes':
        guest.staying = True
    else:
        guest.staying = False

    if request.POST['rehearsal'] == 'yes':
        guest.rehearsal = True
    else:
        guest.rehearsal = False

    if request.POST['color'] == 'yes':
        guest.color_war = True
    else:
        guest.color_war = False

    if not request.POST['shirt'] == 'null':
        guest.shirt_size = request.POST['shirt']
    else:
        guest.shirt_size = None

    guest.save()


    return redirect('/all_guests')

def edit_guest_page(request, guest_id):
    guest = Guest.objects.get(id=guest_id)
    context = {
        'guest':guest
    }
    return render(request, 'form/edit_guest.html', context)

def fill_invites():
    # form id
    # 0 = know both
    # 1 = in house , know both
    # 2 = in house, with guest
    # 3 = lone wolf, no plus
    # 4 = one plus guest
    Invite.objects.create(guest_1 = Guest.objects.get(id=5), guest_2 = Guest.objects.get(id=6), greeting="Mom and Dad Butler", passcode='DJTP', opened=False, form_type=1, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=7), guest_2 = Guest.objects.get(id=8), greeting="Matthew and Sam", passcode='EM1Z', opened=False, form_type=1, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=9), guest_2 = Guest.objects.get(id=10), greeting="Caitlin and Adam", passcode='JDHT', opened=False, form_type=1, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=11), guest_2 = Guest.objects.get(id=12), greeting="Leah and Laura", passcode='C8T8', opened=False, form_type=1, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=13), guest_2 = Guest.objects.get(id=14), greeting="Katie and Devin", passcode='G6NG', opened=False, form_type=1, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=15), guest_2 = Guest.objects.get(id=16), greeting="Molly and Tom", passcode='LPY5', opened=False, form_type=1, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=17), guest_2 = Guest.objects.get(id=18), greeting="Kyra and Cheryl", passcode='RXL3', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=19), greeting="Kelly and Guest", passcode='X2HP', opened=False, form_type=4, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=20), guest_2 = Guest.objects.get(id=21), greeting="Justin and Lauren", passcode='WDG8', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=22), guest_2 = Guest.objects.get(id=23), greeting="Alex and Deirdra", passcode='K3IC', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=24), guest_2 = Guest.objects.get(id=25), greeting="Betsy and Tom", passcode='TNUJ', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=26), guest_2 = Guest.objects.get(id=27), greeting="Josh and Jennette", passcode='ID87', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=28), guest_2 = Guest.objects.get(id=29), greeting="Andy and Lisa", passcode='65UC', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=30), greeting="Debby", passcode='4J36', opened=False, form_type=3, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=31), greeting="Nancy", passcode='Q1AE', opened=False, form_type=3, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=32), guest_2 = Guest.objects.get(id=33), greeting="Diane and Richard", passcode='1JBC', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=34), guest_2 = Guest.objects.get(id=35), greeting="Denny and Monica", passcode='KXWX', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=36), greeting="Susie", passcode='SU45', opened=False, form_type=3, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=37), greeting="Sandy", passcode='GGY7', opened=False, form_type=3, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=38), guest_2 = Guest.objects.get(id=39), greeting="Rick and Adel", passcode='2VFV', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=40), guest_2 = Guest.objects.get(id=41), greeting="Bob and Mary", passcode='PW7D', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=42), greeting="Danny", passcode='X3YN', opened=False, form_type=3, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=43), guest_2 = Guest.objects.get(id=44), greeting="Jeff and Laura", passcode='EBEJ', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=45), guest_2 = Guest.objects.get(id=46), greeting="Anna and Tom", passcode='4M6G', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=47), guest_2 = Guest.objects.get(id=48), greeting="Ryan and Karissa", passcode='AC8U', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=49), guest_2 = Guest.objects.get(id=50), greeting="Cass and Greg", passcode='ZCXL', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=51), greeting="Ashley and Guest", passcode='LM94', opened=False, form_type=4, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=52), guest_2 = Guest.objects.get(id=53), greeting="Mom and Dad Chicirda", passcode='DGP2', opened=False, form_type=1, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=54), guest_2 = Guest.objects.get(id=55), greeting="Tim and Megan", passcode='2GNX', opened=False, form_type=1, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=56), guest_2 = Guest.objects.get(id=57), greeting="Aunt Denise and Uncle Mike", passcode='3FEJ', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=58), guest_2 = Guest.objects.get(id=59), greeting="Michael and Heather", passcode='T9RM', opened=False, form_type=1, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=60), guest_2 = Guest.objects.get(id=61), greeting="Dani and Joey", passcode='P51H', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=62), guest_2 = Guest.objects.get(id=63), greeting="Uncle Nello and Aunt Andrea", passcode='9KN6', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=64), guest_2 = Guest.objects.get(id=65), greeting="Peter and Jeanine", passcode='M1NQ', opened=False, form_type=0, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=66), greeting="Gino and Guest", passcode='WSF3', opened=False, form_type=4, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=67), greeting="Coyne and Guest", passcode='1NQM', opened=False, form_type=2, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=68), guest_2 = Guest.objects.get(id=69), greeting="Miiiiidge and Cat", passcode='KBYH', opened=False, form_type=1, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=70), guest_2 = Guest.objects.get(id=71), greeting="Browntown and Brit", passcode='652M', opened=False, form_type=1, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=72), greeting="Mike and Guest", passcode='RZEF', opened=False, form_type=4, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=73), greeting="Pastor Tyler and Guest", passcode='YYH7', opened=False, form_type=2, completed=False)
    Invite.objects.create(guest_1 = Guest.objects.get(id=74), guest_2 = Guest.objects.get(id=75), greeting="Greg and Dana", passcode='9ZK6', opened=False, form_type=0, completed=False)



def fill_guests():
    Guest.objects.create(first_name = "Gordon", last_name = "Butler", attending=False, staying=False);
    Guest.objects.create(first_name = "Wendy", last_name = "Butler", attending=False, staying=False);
    Guest.objects.create(first_name = "Matthew", last_name = "Butler", attending=False, staying=False);
    Guest.objects.create(first_name = "Sam", last_name = "Butler", attending=False, staying=False);
    Guest.objects.create(first_name = "Caitlin", last_name = "Kownacki", attending=False, staying=False);
    Guest.objects.create(first_name = "Adam", last_name = "Kownacki", attending=False, staying=False);
    Guest.objects.create(first_name = "Leah", last_name = "Kacanda", attending=False, staying=False);
    Guest.objects.create(first_name = "Laura", last_name = "Kacanda", attending=False, staying=False);
    Guest.objects.create(first_name = "Katie", last_name = "Leach", attending=False, staying=False);
    Guest.objects.create(first_name = "Devin", last_name = "Leach", attending=False, staying=False);
    Guest.objects.create(first_name = "Molly", last_name = "Beal", attending=False, staying=False);
    Guest.objects.create(first_name = "Tom", last_name = "Beal", attending=False, staying=False);
    Guest.objects.create(first_name = "Kyra", last_name = "Elizysmith", attending=False, staying=False);
    Guest.objects.create(first_name = "Cheryl", last_name = "Elizysmith", attending=False, staying=False);
    Guest.objects.create(first_name = "Kelly", last_name = "Malampy", attending=False, staying=False);
    Guest.objects.create(first_name = "Justin", last_name = "Mignone", attending=False, staying=False);
    Guest.objects.create(first_name = "Lauren", last_name = "Goldman", attending=False, staying=False);
    Guest.objects.create(first_name = "Alex", last_name = "Arce", attending=False, staying=False);
    Guest.objects.create(first_name = "Deirdra", last_name = "Lahey", attending=False, staying=False);
    Guest.objects.create(first_name = "Betsy", last_name = "Petruzzelli", attending=False, staying=False);
    Guest.objects.create(first_name = "Tom", last_name = "Petruzzelli", attending=False, staying=False);
    Guest.objects.create(first_name = "Josh", last_name = "Petruzzelli", attending=False, staying=False);
    Guest.objects.create(first_name = "Jennette", last_name = "Petruzzelli", attending=False, staying=False);
    Guest.objects.create(first_name = "Andy", last_name = "Petruzzelli", attending=False, staying=False);
    Guest.objects.create(first_name = "Lisa", last_name = "", attending=False, staying=False);
    Guest.objects.create(first_name = "Debby", last_name = "Butler", attending=False, staying=False);
    Guest.objects.create(first_name = "Nancy", last_name = "Butler", attending=False, staying=False);
    Guest.objects.create(first_name = "Diane", last_name = "Kuhlman", attending=False, staying=False);
    Guest.objects.create(first_name = "Richard", last_name = "Kuhlman", attending=False, staying=False);
    Guest.objects.create(first_name = "Denny", last_name = "Shevik", attending=False, staying=False);
    Guest.objects.create(first_name = "Monica", last_name = "Shevik", attending=False, staying=False);
    Guest.objects.create(first_name = "Susie", last_name = "Pruet", attending=False, staying=False);
    Guest.objects.create(first_name = "Sandy", last_name = "Thompson", attending=False, staying=False);
    Guest.objects.create(first_name = "Rick", last_name = "Shevik", attending=False, staying=False);
    Guest.objects.create(first_name = "Adel", last_name = "Shevik", attending=False, staying=False);
    Guest.objects.create(first_name = "Bob", last_name = "Shevik", attending=False, staying=False);
    Guest.objects.create(first_name = "Mary", last_name = "Shevik", attending=False, staying=False);
    Guest.objects.create(first_name = "Danny", last_name = "Thompson", attending=False, staying=False);
    Guest.objects.create(first_name = "Jeff", last_name = "Pruet", attending=False, staying=False);
    Guest.objects.create(first_name = "Laura", last_name = "", attending=False, staying=False);
    Guest.objects.create(first_name = "Anna", last_name = "Brudzinski", attending=False, staying=False);
    Guest.objects.create(first_name = "Tom", last_name = "Brudzinski", attending=False, staying=False);
    Guest.objects.create(first_name = "Ryan", last_name = "Foelske", attending=False, staying=False);
    Guest.objects.create(first_name = "Karissa", last_name = "Foelske", attending=False, staying=False);
    Guest.objects.create(first_name = "Cass", last_name = "Stephenson", attending=False, staying=False);
    Guest.objects.create(first_name = "Greg", last_name = "Stephenson", attending=False, staying=False);
    Guest.objects.create(first_name = "Ashley", last_name = "Legel", attending=False, staying=False);
    Guest.objects.create(first_name = "Timothy", last_name = "Chicirda", attending=False, staying=False);
    Guest.objects.create(first_name = "Florence", last_name = "Chicirda", attending=False, staying=False);
    Guest.objects.create(first_name = "Tim", last_name = "Chicirda", attending=False, staying=False);
    Guest.objects.create(first_name = "Megan", last_name = "Chicirda", attending=False, staying=False);
    Guest.objects.create(first_name = "Denise", last_name = "McGuigan", attending=False, staying=False);
    Guest.objects.create(first_name = "Mike", last_name = "McGuigan", attending=False, staying=False);
    Guest.objects.create(first_name = "Michael", last_name = "McGuigan", attending=False, staying=False);
    Guest.objects.create(first_name = "Heather", last_name = "McGuigan", attending=False, staying=False);
    Guest.objects.create(first_name = "Dani", last_name = "D'Aquila", attending=False, staying=False);
    Guest.objects.create(first_name = "Joey", last_name = "D'Aquila", attending=False, staying=False);
    Guest.objects.create(first_name = "Nello", last_name = "Naticchione", attending=False, staying=False);
    Guest.objects.create(first_name = "Andrea", last_name = "Naticchione", attending=False, staying=False);
    Guest.objects.create(first_name = "Peter", last_name = "Naticchione", attending=False, staying=False);
    Guest.objects.create(first_name = "Jeanine", last_name = "Naticchione", attending=False, staying=False);
    Guest.objects.create(first_name = "Gino", last_name = "Naticchione", attending=False, staying=False);
    Guest.objects.create(first_name = "Dan", last_name = "Coyne", attending=False, staying=False);
    Guest.objects.create(first_name = "Mark", last_name = "Bartholomew", attending=False, staying=False);
    Guest.objects.create(first_name = "Catherine", last_name = "", attending=False, staying=False);
    Guest.objects.create(first_name = "Tim", last_name = "Brown", attending=False, staying=False);
    Guest.objects.create(first_name = "Brittany", last_name = "Brown", attending=False, staying=False);
    Guest.objects.create(first_name = "Mike", last_name = "Alfonso", attending=False, staying=False);
    Guest.objects.create(first_name = "Tyler", last_name = "Cunnion", attending=False, staying=False);
    Guest.objects.create(first_name = "Greg", last_name = "Hager", attending=False, staying=False);
    Guest.objects.create(first_name = "Dana", last_name = "Hager", attending=False, staying=False);
