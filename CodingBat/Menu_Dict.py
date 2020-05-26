menu = {'category_id': 'LE4488-2', 'category_type': 'dealBuilderSub', 'config_code': 'LE_National_5NUP',
        'creative_code': 'LE_5NUP', 'description': '', 'image': 'PZone_5LU_MobileIcon_48x48.png', 'min_required': 1,
        'name': "P'Zone", 'num_free_tops': 1, 'products': [{'product_id': 'NTLELINEUP~SW^LE^ZP^^~830'}],
        'sub_categories': []}

menu_2 = {'category_id': 'LE4488-0', 'category_type': 'dealBuilderSub', 'config_code': 'LE_National_5NUP',
          'creative_code': 'LE_5NUP', 'description': '', 'image': 'PH_Pizza_Mobile_Menu_Final_48x48.png',
          'min_required': 1, 'name': 'Pizza', 'num_free_tops': 1,
          'products': [{'product_id': 'NTLELINEUP~P^BY~830'}, {'display_order': 1, 'product_id': 'NTLELINEUP~P^BF~830'},
                       {'display_order': 2, 'product_id': 'NTLELINEUP~P^CB~830'},
                       {'display_order': 3, 'product_id': 'NTLELINEUP~P^B~830'},
                       {'display_order': 4, 'product_id': 'NTLELINEUP~P^HK~830'},
                       {'display_order': 5, 'product_id': 'NTLELINEUP~P^ML~830'},
                       {'display_order': 6, 'product_id': 'NTLELINEUP~P^PL~830'},
                       {'display_order': 7, 'product_id': 'NTLELINEUP~P^SS~830'},
                       {'display_order': 8, 'product_id': 'NTLELINEUP~P^S~830'},
                       {'display_order': 9, 'product_id': 'NTLELINEUP~P^UC~830'},
                       {'display_order': 10, 'product_id': 'NTLELINEUP~P^VL~830'}], 'sub_categories': []}

NEW_LINEUP_CONFIG_CODE = "LE_5NUP"
lineup_categories = []

if NEW_LINEUP_CONFIG_CODE in menu.values():
    lineup_categories.append(menu)
    if NEW_LINEUP_CONFIG_CODE in menu_2.values():
        lineup_categories.append(menu_2)

print(lineup_categories)
