from bs4 import BeautifulSoup, SoupStrainer

sr = '<form method="post" action="/login/device-based/validate-pin/?refid=8" id="u_0_2_zc"><input type="hidden" name="lsd" value="AVpRop29CxI" autocomplete="off"><input type="hidden" name="jazoest" value="2935" autocomplete="off"><input type="hidden" name="uid" value="61551911035142"><input type="hidden" name="flow" value="login_no_pin"><input type="hidden" name="next" value=""><div class="_af7v" role="button" aria-label="Ketuk untuk masuk ke Facebook sebagai Subh Enrj. Pengguna ini memiliki 1 notifikasi baru" tabindex="0" id="u_0_3_LB"><span class="_52je _52jb _52jg _2t_z"><div><div>Subh Enrj</div></div></span></div></form>'


form = BeautifulSoup(sr, "html.parser", parse_only=SoupStrainer('form'))
if pattern := form.select_one('form[action*="/login/device-based/validate-pin/"]'):
    print('login saver found, handle it')



exit()

html = BeautifulSoup(sr, "html.parser")

if pattern := html.select_one('form[action*="/login/device-based/validate-pin/"]'):
	print('login saver found, handle it')

	print('get div button id from form')
	btnid = pattern.find('div', {'role': 'button'})['id']
	print(btnid)


# soup = BeautifulSoup(html)
# try:
#     value = soup.find('input', {'id': 'xyz'}).get('value')
# except Exception as e:
#     print("Got unhandled exception %s" % str(e))
