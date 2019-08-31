import requests
import csv_io

# Authorization: Bearer b951b427c982491c98d6077af4539740

# token = 'b951b427c982491c98d6077af4539740'
# # version_test = '1.2'
# version = '1.0'
#
# url_of_getting_lists_of_firms = 'http://api.ati.su/v1.0/lists/firms?access_token=b951b427c982491c98d6077af4539740'
#
# url_of_getting_by_listId_Alapaevsk = 'http://api.ati.su/v1.0/lists/firms/13d91cb4-90c1-e911-bb99-0cc47af30c1b?access_token=b951b427c982491c98d6077af4539740'
#
# list_id_Alapaevsk = '13d91cb4-90c1-e911-bb99-0cc47af30c1b'


def get_contacts_by_id(all_contacts, ati_id):
    get_contacts_method = 'http://api.ati.su/v1.0/firms/' + str(ati_id) + '/contacts/summary?access_token=b951b427c982491c98d6077af4539740'
    response = requests.get(get_contacts_method)

    data = response.json()

    # print(data)

    for contact in data:
        ownership = contact['ownership']

        firm_name = contact['ownership'] + ' ' + contact['firm_name']
        ati_id = contact['ati_id']
        name = 'п' + contact['city'] + ' ' + contact['name']
        mobile_phone = contact['mobile_phone']

        if mobile_phone != '':
            all_contacts.append([name, mobile_phone, firm_name])


def get_value():
    for i in range(1, 1000):
        value = '2_' + str(i)
        print(value)


def write_contacts(url):
    response = requests.get(url)
    data = response.json()

    firms_count = data['data']['totalFirmsCount']
    all_contacts = []

    if firms_count > 0:
        for i in range(firms_count):                                                                                                     # CHECK THIS
            profile = data['data']['firms'][i]['firm']['profile']

            if profile == 'Экспедитор-перевозчик' or profile == 'Перевозчик' or profile == 'Грузовладелец-перевозчик':
                ati_id = data['data']['firms'][i]['firm']['id']
                get_contacts_by_id(all_contacts, ati_id)

        city_name = data['data']['firms'][0]['firm']['fullCityName']
        print(city_name)

        csv_io.write([['Name', 'Mobile Phone', 'Company']], '/Users/egornikulin/Desktop/DB-ati/' + city_name + '.csv')
        csv_io.write_a(all_contacts, '/Users/egornikulin/Desktop/DB-ati/' + city_name + '.csv')                                              # CHECK PATH


# print('Введите url: ')
# url = input()
# write_contacts(url)


# if '__name__' == '__main__':
#     main()


# rating_url_alapaevsk = 'https://ati.su/api/rating/getFirmsRating?filter={"PageNumber":1,"ItemsPerPage":10000,"IsReverse":0,"Geo":{"value":"2_3332","text":"Алапаевск,+Свердловская+область,+Россия","disabled":false},"FirmTypes":[],"IsActiveMemberAtiDoc":0,"IsTribunalUser":0,"HasDisplayedAutoparkItems":0,"HasAtiOrders":0}'

rating_url_moscow = 'https://ati.su/api/rating/getFirmsRating?filter={"PageNumber":1,"ItemsPerPage":5578,"IsReverse":0,"Geo":{"value":"1_151","text":"Москва (регион), Россия","disabled":false},"FirmTypes":[],"IsActiveMemberAtiDoc":0,"IsTribunalUser":0,"HasDisplayedAutoparkItems":0,"HasAtiOrders":0}'
rating_url_tlt = 'https://ati.su/api/rating/getFirmsRating?filter={"PageNumber":1,"ItemsPerPage":10000,"IsReverse":0,"Geo":{"value":"2_253","text":"Тольятти, Самарская область, Россия","disabled":false},"FirmTypes":[],"IsActiveMemberAtiDoc":0,"IsTribunalUser":0,"HasDisplayedAutoparkItems":0,"HasAtiOrders":0}'
rating_url_kolomna = 'https://ati.su/api/rating/getFirmsRating?filter={"PageNumber":1,"ItemsPerPage":10000,"IsReverse":0,"Geo":{"value":"2_107","text":"Коломна, Московская область, Россия","disabled":false},"FirmTypes":[],"IsActiveMemberAtiDoc":0,"IsTribunalUser":0,"HasDisplayedAutoparkItems":0,"HasAtiOrders":0}'
rating_url_spb = 'https://ati.su/api/rating/getFirmsRating?filter={"PageNumber":1,"ItemsPerPage":10000,"IsReverse":0,"Geo":{"value":"2_1","text":"","disabled":false},"FirmTypes":[],"IsActiveMemberAtiDoc":0,"IsTribunalUser":0,"HasDisplayedAutoparkItems":0,"HasAtiOrders":0}'
rating_url_syzran = 'https://ati.su/api/rating/getFirmsRating?filter={"PageNumber":1,"ItemsPerPage":10000,"IsReverse":0,"Geo":{"value":"2_245","text":"Сызрань, Самарская область, Россия","disabled":false},"FirmTypes":[],"IsActiveMemberAtiDoc":0,"IsTribunalUser":0,"HasDisplayedAutoparkItems":0,"HasAtiOrders":0}'

urls = ['https://ati.su/api/rating/getFirmsRating?filter={"PageNumber":1,"ItemsPerPage":5578,"IsReverse":0,"Geo":{"value":"1_151","text":"Москва (регион), Россия","disabled":false},"FirmTypes":[],"IsActiveMemberAtiDoc":0,"IsTribunalUser":0,"HasDisplayedAutoparkItems":0,"HasAtiOrders":0}',
        'https://ati.su/api/rating/getFirmsRating?filter={"PageNumber":1,"ItemsPerPage":10000,"IsReverse":0,"Geo":{"value":"2_253","text":"Тольятти, Самарская область, Россия","disabled":false},"FirmTypes":[],"IsActiveMemberAtiDoc":0,"IsTribunalUser":0,"HasDisplayedAutoparkItems":0,"HasAtiOrders":0}',
        'https://ati.su/api/rating/getFirmsRating?filter={"PageNumber":1,"ItemsPerPage":10000,"IsReverse":0,"Geo":{"value":"2_107","text":"Коломна, Московская область, Россия","disabled":false},"FirmTypes":[],"IsActiveMemberAtiDoc":0,"IsTribunalUser":0,"HasDisplayedAutoparkItems":0,"HasAtiOrders":0}',
        'https://ati.su/api/rating/getFirmsRating?filter={"PageNumber":1,"ItemsPerPage":10000,"IsReverse":0,"Geo":{"value":"2_1","text":"","disabled":false},"FirmTypes":[],"IsActiveMemberAtiDoc":0,"IsTribunalUser":0,"HasDisplayedAutoparkItems":0,"HasAtiOrders":0}',
        'https://ati.su/api/rating/getFirmsRating?filter={"PageNumber":1,"ItemsPerPage":10000,"IsReverse":0,"Geo":{"value":"2_245","text":"Сызрань, Самарская область, Россия","disabled":false},"FirmTypes":[],"IsActiveMemberAtiDoc":0,"IsTribunalUser":0,"HasDisplayedAutoparkItems":0,"HasAtiOrders":0}']


def main():
    values = ['1_151', '2_253', '2_107', '2_1', '2_245']

    for i in range(363, 1000):                                                                                               # CHECK RANGE
        value = '2_' + str(i)
        if value not in values:
            url = 'https://ati.su/api/rating/getFirmsRating?filter={' \
                  '"PageNumber":1,"ItemsPerPage":10000,"IsReverse":0,"Geo":{' \
                  '"value":"' + value + '","text":"","disabled":false},' \
                  '"FirmTypes":[],"IsActiveMemberAtiDoc":0,"IsTribunalUser":0,' \
                  '"HasDisplayedAutoparkItems":0,"HasAtiOrders":0}'
            write_contacts(url)


main()
