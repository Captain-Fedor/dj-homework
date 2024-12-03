d = [
    {'id': '1', 'name': 'Samsung Galaxy Edge 2', 'image': 'https://avatars.mds.yandex.net/get-mpic/364668/img_id5636027222104023144.jpeg/orig', 'price': '73000', 'release_date': '2016-12-12', 'lte_exists': 'True'},
    {'id': '2', 'name': 'Iphone X', 'image': 'https://avatars.mds.yandex.net/get-mpic/200316/img_id270362589725797013.png/orig', 'price': '80000', 'release_date': '2017-06-01', 'lte_exists': 'True'},
    {'id': '3', 'name': 'Nokia 8', 'image': 'https://avatars.mds.yandex.net/get-mpic/397397/img_id6752445806321208103.jpeg/orig', 'price': '20000', 'release_date': '2013-01-20', 'lte_exists': 'False'}
]

dc = {'id': '1', 'name': 'Samsung Galaxy Edge 2',
      'image': 'https://avatars.mds.yandex.net/get-mpic/364668/img_id5636027222104023144.jpeg/orig',
      'price': '73000', 'release_date': '2016-12-12', 'lte_exists': 'True'}
for key, value in dc.items():
    print(f'{key} = {value}')

