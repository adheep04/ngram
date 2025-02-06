from pprint import pprint

# get dicts
ch_to_id = {c : i for i, c in enumerate('^$abcdefghijklmnopqrstuvwxyz0123456789')}
ch_to_id['<s>'] = ch_to_id.pop('^')
ch_to_id['<e>'] = ch_to_id.pop('$')
id_to_ch = {ch_to_id[i] : i for i in ch_to_id.keys()}

