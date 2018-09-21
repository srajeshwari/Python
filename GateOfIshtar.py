import time,re
from datetime import datetime

p_d_t = datetime.now()

champion_initial_health = {'human' : 100, 'wizard' : 100, 'spirit' : 100, 'giant' : 150, 'vampire' : 110}


def champion_health(champ):
    """
    Validates the champion and the start/end time and date
    """
    if champ in ['wizard', 'spirit']:
        print "Magical champion"
        return champion_initial_health[champ]

    e_d_t = p_d_t.replace(day = int(d.groups()[0]), month = int(d.groups()[1]), year = int(d.groups()[2]),
                          hour = int(t.groups()[0]), minute = int(t.groups()[1]))
    if e_d_t < p_d_t:
        print "Invalid end_date_time, end_date_time should be greater than present date and time"
        return None
    elif e_d_t >= p_d_t:
        print "Obtained Valid date and time"
        return loss_calculation(champ, e_d_t) 
    
def loss_calculation(champ_type, f_d_t):
    """
    Calculates the loss of the champion for every 1 hour
    """
    in_champ_val = champion_initial_health[champ_type]
    i_d_t = p_d_t

    while i_d_t <= f_d_t:

        if i_d_t.strftime("%A") in ["Tuesday", "Thursday"]:
            print "No Loss day : ", i_d_t
        else:
            while i_d_t.hour <= 23 and i_d_t <= f_d_t:
                if i_d_t.hour == 6 and i_d_t.minute in range(0,30):
                    # "Janna" demon of Wind spawned
                    in_champ_val = in_champ_val - 7
                elif i_d_t.hour == 6 and i_d_t.minute in range(30,60):
                    print "In 6 hr and range 30-60 min"
                    # "Tiamat" goddess of Oceans spawned
                    in_champ_val = in_champ_val - 18
                elif i_d_t.hour == 7 and i_d_t.minute in range(0,60):
                    print "In 7 hr and range 0-60 min"
                    # "Mithra" goddess of sun spawned
                    in_champ_val = in_champ_val - 25
                elif i_d_t.hour == 8 and i_d_t.minute in range(0,30):
                    print "In 8 hr and range 0-30 min"
                    # "Warwick" God of war spawned
                    in_champ_val = in_champ_val - 18
                elif i_d_t.hour == 8 and i_d_t.minute in range(30,60):
                    print "In 8 hr and range 30-60 min"
                    # "Kalista" demon of agony spawned
                    in_champ_val = in_champ_val - 7
                elif i_d_t.hour == 14 and i_d_t.minute in range(30,60):
                    print "In 14 hr and range 30-60 min"
                    # "Kalista" demon of agony spawned
                    in_champ_val = in_champ_val - 7
                elif i_d_t.hour == 15 and i_d_t.minute in range(0,30):
                    print "In 15 hr and range 0-30 min"
                    # "Ahri" goddess of wisdom spawned
                    in_champ_val = in_champ_val - 13
                elif i_d_t.hour == 15 and i_d_t.minute in range(30,60):
                    print "In 15 hr and range 30-60 min"
                    # "Brand" god of fire spawned
                    in_champ_val = in_champ_val - 25
                elif i_d_t.hour == 16 and i_d_t.minute in range(0,60):
                    print "In 16 hr and range 0-60 min"
                    # "Brand" god of fire spawned
                    in_champ_val = in_champ_val - 25
                elif i_d_t.hour == 17 and i_d_t.minute in range(0,60):
                    print "In 17 hr and range 0-60 min"
                    # "Rumble" god of lightning spawned
                    in_champ_val = in_champ_val - 18
                elif i_d_t.hour == 18 and i_d_t.minute in range(0,60):
                    print "In 18 hr and range 0-60 min"
                    # "Skarner" the scorpion demon spawned
                    in_champ_val = in_champ_val - 7
                elif i_d_t.hour == 19 and i_d_t.minute in range(0,60):
                    print "In 19 hr and range 30-60 min"
                    # "Skarner" the scorpion demon spawned
                    in_champ_val = in_champ_val - 7
                elif i_d_t.hour == 20 and i_d_t.minute in range(0,60):
                    print "In 20 hr and range 0-60 min"
                    # "Luna" The goddess of the moon spawned
                    in_champ_val = in_champ_val - 13
                else:
                    pass

                if i_d_t.hour == 23 or i_d_t >= f_d_t:
                    break
                else:
                    i_d_t = i_d_t.replace(hour = i_d_t.hour+1)

                
        i_d_t = i_d_t.replace(day = i_d_t.day+1, hour = 00)

    if in_champ_val < 0:
        return 0
    else:
        return in_champ_val

if __name__ == '__main__':
    """
    Validates champion name and the end date and time
    The start date and time will be the current date and time 
    """
    valid = 'Yes'
    
    def main():
        champion = raw_input("Enter valid champion name as : wizard/spirit/human/giant/vampire : ")
        champion = champion.lower()
        global champion,d,t
        if champion not in champion_initial_health:
            print "Try again with valid champion name"
            return 'No'
        else :
            print "The START date and time will be : ", p_d_t
            end_date = raw_input("Provide the champion END date in dd-mm-yyyy format : ")
            d = re.match('(\d{2})[-](\d{2})[-](\d{4})', end_date)

            end_time = raw_input("Provide the END time in hr:mm format :  ")
            t = re.match('(\d{2})[:](\d{2})', end_time)
            if d == None or t == None:
                print "Invalid date/time , try again "
                return 'No'                
        return 'Yes'
    
    while True :        
        valid = main()
        if valid == 'Yes':
            break

    final_health = champion_health(champion)
    print "Final health present in the champion is : ", final_health

    
        
                
