import json

acceptance_rates = []

def load_acceptance_rate():
	acl_data = open('./data/ACL/acceptance_rate.json','r')
	cvpr_data = open('./data/CVPR/acceptance_rate.json', 'r')
	emnlp_data = open('./data/EMNLP/acceptance_rate.json', 'r')
	iclr_data = open('./data/ICLR/acceptance_rate.json','r')
	icml_data = open('./data/ICML/acceptance_rate.json', 'r')
	nips_data = open('./data/NIPS/acceptance_rate.json', 'r')

	acl = json.load(acl_data)
	cvpr = json.load(cvpr_data)
	emnlp = json.load(emnlp_data)
	iclr = json.load(iclr_data)
	icml = json.load(icml_data)
	nips = json.load(nips_data)

	acceptance_rates.append(acl)
	acceptance_rates.append(cvpr)
	acceptance_rates.append(emnlp)
	acceptance_rates.append(iclr)
	acceptance_rates.append(icml)
	acceptance_rates.append(nips)

load_acceptance_rate()
