import json

conferences = []

def load_conference():
	acl_data = open('./data/ACL/conference.json','r')
	cvpr_data = open('./data/CVPR/conference.json', 'r')
	emnlp_data = open('./data/EMNLP/conference.json', 'r')
	iclr_data = open('./data/ICLR/conference.json','r')
	icml_data = open('./data/ICML/conference.json', 'r')
	nips_data = open('./data/NIPS/conference.json', 'r')

	acl = json.load(acl_data)
	cvpr = json.load(cvpr_data)
	emnlp = json.load(emnlp_data)
	iclr = json.load(iclr_data)
	icml = json.load(icml_data)
	nips = json.load(nips_data)

	conferences.append(acl)
	conferences.append(cvpr)
	conferences.append(emnlp)
	conferences.append(iclr)
	conferences.append(icml)
	conferences.append(nips)

load_conference()
