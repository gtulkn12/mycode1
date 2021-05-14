#!/usr/bin/env python3
def main():
        global data
        status = " "
        q= ""

        data= {
        'Questions' : {
                'Friday' : 'What are you most likely doing on a Friday night? ',
                'Songlist' : 'What is your favorite song? '
                },
        'Friday' : {
                1 : ['Staying in the house', 'relaxing at home'],
                2 : ['At a house party', 'going out to 90\'s theme house parties'],
                3 : ['At the club with friends', 'hitting the streets'],
                4 : ['Watching NetFlix w/ my S.O.', 'spending quality time with your partner']
                },

        'SongList' : {
                1 : ['Nate Dog', 'Regulate by Nate Dog'],
                2 : ['Onyx', 'Slam by Onyx'],
                3 : ['Salt-N-Peppa', 'Shoop by Salt-N-Peppa'],
                4 : ['MC Hammer', 'Can\'t touch this by MC Hammer']
                }
        }

        while status:
                fridayoptions= display_options(data["Friday"])
                songoptions= display_options(data["SongList"])
                try:
                        friday_answer= int(input(f"{data['Questions']['Friday']}\n{fridayoptions}> "))
                        if friday_answer not in data["Friday"].keys():
                            print("***** Invalid entry, please try Again *****")
                            continue

                        song_answer= int(input(f"\n{data['Questions']['Songlist']}\n{songoptions}>"))
                        if song_answer not in data["SongList"].keys():
                            print("***** Invalid entry, please try Again *****")
                            continue
                        status = False;
                except ValueError:
                        print("\n***** Invalid entry, please try Again *****")
        print(f"\nIt is apparent you enjoy {data['Friday'][friday_answer][1]} and listening to {data['SongList'][song_answer][1]} ")

def display_options(data):
        options= data
        choice= "\n"
        for key in options:
                choice += f"{key} {options[key][0]}\n"
        return choice

main()
