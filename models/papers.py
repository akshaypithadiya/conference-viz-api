import json

papers_list = []

def load_keywords():
	acl_data = open('./data/ACL/papers.json','r')
	cvpr_data = open('./data/CVPR/papers.json', 'r')
	emnlp_data = open('./data/EMNLP/papers.json', 'r')
	iclr_data = open('./data/ICLR/papers.json','r')
	icml_data = open('./data/ICML/papers.json', 'r')
	nips_data = open('./data/NIPS/papers.json', 'r')

	acl = json.load(acl_data)
	cvpr = json.load(cvpr_data)
	emnlp = json.load(emnlp_data)
	iclr = json.load(iclr_data)
	icml = json.load(icml_data)
	nips = json.load(nips_data)

	papers_list.append(acl)
	papers_list.append(cvpr)
	papers_list.append(emnlp)
	papers_list.append(iclr)
	papers_list.append(icml)
	papers_list.append(nips)
	
load_keywords()
