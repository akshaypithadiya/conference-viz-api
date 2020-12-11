import json

keywords_list = []

def load_keywords():
	acl_data = open('./data/ACL/keywords.json','r')
	cvpr_data = open('./data/CVPR/keywords.json', 'r')
	emnlp_data = open('./data/EMNLP/keywords.json', 'r')
	iclr_data = open('./data/ICLR/keywords.json','r')
	icml_data = open('./data/ICML/keywords.json', 'r')
	nips_data = open('./data/NIPS/keywords.json', 'r')

	acl = json.load(acl_data)
	cvpr = json.load(cvpr_data)
	emnlp = json.load(emnlp_data)
	iclr = json.load(iclr_data)
	icml = json.load(icml_data)
	nips = json.load(nips_data)

	keywords_list.append(acl)
	keywords_list.append(cvpr)
	keywords_list.append(emnlp)
	keywords_list.append(iclr)
	keywords_list.append(icml)
	keywords_list.append(nips)
	
load_keywords()
