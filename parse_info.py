import json
with open('text1.txt', 'r') as file:
    data = file.readlines()

std_form = []
towns = [[] for _ in range(32)]
ind = -1
for line in data:
    if ")" not in line[:3]:
        towns[ind].append(line[:-1])
    else:
        ind+=1
        towns[ind].append(line[:-1])

for i,town in enumerate(towns[:23]):
    std_form.append({})
    std_form[i]["протопресвітерат"] = towns[-1][1].rstrip("(").split()[0]
    std_form[i]["деканат"] = towns[-1][0].split()[1]
    std_form[i]["населений пункт"] = {}
    std_form[i]["населений пункт"]["назва"] = town[0].split()[1],
    std_form[i]["населений пункт"]["location"] = {'lat': -10, 'lng':-20}
    num_churches = town[0].count('ц.')
    std_form[i]['церкви'] = [{} for _ in range(num_churches)]
    for j in range(num_churches):
        std_form[i]['церкви'][j]['назва'] = town[0].split('ц.')[1].split(',')[0]
        try:
            std_form[i]['церкви'][j]['тип'] = town[0].split('ц.')[1].split(',')[1].split()[0]
            std_form[i]['церкви'][j]['рік'] =  town[0].rstrip('ц.').split(',')[1].split()[1]
        except IndexError:
            print(f'No info for {town[0]}')


    if 'Надає' in town[1]:
        std_form[i]['надає'] = {'назва': town[1].split(":")[1]}
    std_form[i]["персонал"] = {}
    for j,inline in enumerate(town):
        if 'Душ:' in inline or "Дот:" in inline:
            stop_pers = j
            break
    for inline in town[1:stop_pers]:
        if 'Надає' not in inline:
            std_form[i]['персонал'][inline.split(':')[0]] = inline.split(':')[1]


    start_dush = -1
    for j,inline in enumerate(town):
        if "Душ" in inline:
            start_dush = j
    if start_dush!=-1:
        num_lans = town[start_dush].count(';')
        lans = town[start_dush].lstrip("Душ:").split(';')
        std_form[i]['душ'] = [{} for _ in range(num_lans+1)]
        for j,lan in enumerate(lans):
            for z in lan.split(','):
                try:
                    std_form[i]['душ'][j][z.split()[0]] = z.split()[1]
                except IndexError:
                    print('no lan')


    start_dot = -1
    for j, inline in enumerate(town):
        if 'Дот.:' in inline:
            start_dot = j
    if start_dot != -1:
        dot_items = town[start_dot].lstrip("Дот.: ").split(',')
        std_form[i]['дот'] = {}
        for z,dot_item in enumerate(dot_items):
            try:
                std_form[i]['дот'][dot_item.split()[0]] = {}
                for k in range(len(dot_item.split()[1:])//2):
                    std_form[i]['дот'][dot_item.split()[0]][dot_item.split()[1:][2*k]] = dot_item.split()[1:][2*k+1]
            except IndexError:
                print('Дот проблеми')

    start_sch = -1
    for j, inline in enumerate(town):
        if 'Шк.:' in inline:
            start_sch = j
    if start_sch != -1:
        schools = town[start_sch].lstrip('Шк.: ').split(';')
        std_form[i]['навчальні заклади'] = {}
        std_form[i]['навчальні заклади']['шк'] = [{} for _ in range(len(schools))] 

    start_star = -1
    for j, inline in enumerate(town):
        if 'Стар.:' in inline:
            start_star = j
    if start_star != -1:
        std_form[i]['стар.'] = [{} for _ in range(4)]



            
    
print(std_form)
with open("txt1.json", "w") as filer:
            json.dump(std_form, filer, indent=4, ensure_ascii = False)


# std_form["деканат"] = data[0].split()[1]
# std_form["протопресвітерат"] = data[1].lstrip("(").split()[0]
# std_form["населелний пункт"] = {}
# print(std_form)