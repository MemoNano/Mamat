"""
I am trying to define a procedure, involved(courses, person), that takes as input a courses structure and a person and
 returns a Dictionary that describes all the courses the person is involved in.
"""

courses = {
    'feb2012': {'cs101': {'name': 'Building a Search Engine',
                          'teacher': 'Dave',
                          'assistant': 'Peter C.'},
                'cs373': {'name': 'Programming a Robotic Car',
                          'teacher': 'Sebastian',
                          'assistant': 'Andy'}},
    'apr2012': {'cs101': {'name': 'Building a Search Engine',
                          'teacher': 'Dave',
                          'assistant': 'Sarah'},
                'cs212': {'name': 'The Design of Computer Programs',
                          'teacher': 'Peter N.',
                          'assistant': 'Andy',
                          'prereq': 'cs101'},
                'cs253':
                    {'name': 'Web Application Engineering - Building a Blog',
                     'teacher': 'Steve',
                     'prereq': 'cs101'},
                'cs262':
                    {'name': 'Programming Languages - Building a Web Browser',
                     'teacher': 'Wes',
                     'assistant': 'Peter C.',
                     'prereq': 'cs101'},
                'cs373': {'name': 'Programming a Robotic Car',
                          'teacher': 'Sebastian'},
                'cs387': {'name': 'Applied Cryptography',
                          'teacher': 'Dave'}},
    'jan2044': {'cs001': {'name': 'Building a Quantum Holodeck',
                          'teacher': 'Dorina'},
                'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                          'teacher': 'Jasper'},
                }
}


def involed(courses1, person):
    for time1 in courses1:
        # print(time1)
        for course in courses1[time1]:
            # print(course)
            for user in courses1[time1][course]:
                # print(user)
                if user == person:
                    print(user)
            break


if __name__ == '__main__':
    involed(courses, "Dave")

# {'results': [{'address_components': [{'long_name': '595 Market Street',
#                                       'short_name': '595 Market Street',
#                                       'types': ['premise']},
#                                      {'long_name': '595',
#                                       'short_name': '595',
#                                       'types': ['street_number']},
#                                      {'long_name': 'Market Street',
#                                       'short_name': 'Market St',
#                                       'types': ['route']},
#                                      {'long_name': 'South Beach',
#                                       'short_name': 'South Beach',
#                                       'types': ['neighborhood', 'political']},
#                                      {'long_name': 'San Francisco',
#                                       'short_name': 'SF',
#                                       'types': ['locality', 'political']},
#                                      {'long_name': 'San Francisco County',
#                                       'short_name': 'San Francisco County',
#                                       'types': ['administrative_area_level_2',
#                                                 'political']},
#                                      {'long_name': 'California',
#                                       'short_name': 'CA',
#                                       'types': ['administrative_area_level_1',
#                                                 'political']},
#                                      {'long_name': 'United States',
#                                       'short_name': 'US',
#                                       'types': ['country', 'political']},
#                                      {'long_name': '94105',
#                                       'short_name': '94105',
#                                       'types': ['postal_code']}],
#               'formatted_address': '595 Market Street, 595 Market St, San '
#                                    'Francisco, CA 94105, USA',
#               'geometry': {'bounds': {'northeast': {'lat': 37.7895101,
#                                                     'lng': -122.4004556},
#                                       'southwest': {'lat': 37.7889683,
#                                                     'lng': -122.4011435}},
#                            'location': {'lat': 37.7892151, 'lng': -122.4007997},
#                            'location_type': 'ROOFTOP',
#                            'viewport': {'northeast': {'lat': 37.7905881802915,
#                                                       'lng': -122.3994505697085},
#                                         'southwest': {'lat': 37.78789021970851,
#                                                       'lng': -122.4021485302915}}},
#               'place_id': 'ChIJOctshWKAhYARZi7laAtM50A',
#               'types': ['premise']}],
#  'status': 'OK'}

for address1 in result:
            print(address1)