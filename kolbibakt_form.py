#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms import ValidationError
from wtforms.validators import Required, NumberRange, Regexp



def luhn_check(form, field):
	s = field.data[2:]
	try:
		if sum(map(lambda x: x%10 + int(x/10), map(lambda x,y: x*y, map(int, s), [2,1]*5))) % 10 != 0:
			raise ValidationError('Inte ett korrekt personnummer')
	except:
		raise ValidationError('Inte ett korrekt personnummer')


class MainForm(Form):

	snr = IntegerField(label=u'SNR-nummer')
	pnum_regex = Regexp('^[0-9][0-9][0-9][0-9](0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[0-9]{4}$')
	pnumber = StringField(label=u'Personnummer', description=u'ÅÅÅÅMMDDXXXX', validators=[pnum_regex, Required(), luhn_check])

	asa = SelectField(label='ASA', choices=[('1', u'1 - Frisk'),
											('2', u'2 - Mild systemsjukdom'),
											('3', u'3 - Svår systemsjukdom'),
											('4', u'4 - Svår konstant livshotande systemsjukdom')])

	earlier_col = SelectField(label=u'Tidigare kolonoskopi', choices=[('', u'Nej'),
																('A', u'Inom ett år'),
																('B', u'Inom 2-5 år')])

	col_reason = StringField(u'Kolonoskopiorsak')

	bowl_prep = SelectField(u'Tarmförberedelse', choices=[('A', u'Laxabon'),
														('B', u'Phosforal'),
														('C', u'Endast Klyx')])

	full_col = SelectField(u'Full kolonoskopi', choices=[('yes', u'Ja - Identifikation av cekalpol'),
														('no', u'Nej - Ej idendifikation av cekalpol')])

	feac_culture = StringField(label=u'Feacesodling', description=u'Scanna streckkod på rör')

	main_diagnosis = SelectField(label=u'Huvuddiagnos', choices=[('healthy', 'Frisk'),
																('ibd', 'IBD'),
																('cancer', 'Cancer'),
																('polyp', 'Polyp'),
																('diverticulosis', 'Divertikulos')])
	dna_healthy_ceakum = StringField(u'DNA:Frisk Caekum', description=u'Scanna streckkod på rör')
	culture_healthy_ceakum = StringField(u'Odling: Frisk Caekum', description=u'Scanna streckkod på rör')
	dna_healthy_sigma = StringField(u'DNA:Frisk Sigma', description=u'Scanna streckkod på rör')
	culture_healthy_sigma = StringField(u'Odling: Frisk Sigma', description=u'Scanna streckkod på rör')

	dna_polyp = StringField(u'DNA:Polyp >1cm', description=u'Scanna streckkod på rör')
	dna_polyp_loc = SelectField('', choices=[('C', 'Caekum'),
											('T', 'Transversum'),
											('D', 'Descendens'),
											('R', 'Rektum'),
											('A', 'Ascendens')])


	dna_close_polyp = StringField(u'DNA:Nära Polyp > 1 cm', description=u'Scanna streckkod på rör')
	dna_close_polyp_loc = SelectField('', choices=[('C', 'Caekum'),
													('T', 'Transversum'),
													('D', 'Descendens'),
													('R', 'Rektum'),
													('A', 'Ascendens')])


	culture_close_polyp = StringField(u'Odling:Nära Polyp > 1 cm', description=u'Scanna streckkod på rör')
	culture_close_polyp_loc = SelectField('', choices=[('C', 'Caekum'),
													('T', 'Transversum'),
													('D', 'Descendens'),
													('R', 'Rektum'),
													('A', 'Ascendens')])



	dna_cancer = StringField(u'DNA:Cancer', description=u'Scanna streckkod på rör')
	dna_cancer_loc = SelectField('', choices=[('C', 'Caekum'),
												('T', 'Transversum'),
												('D', 'Descendens'),
												('R', 'Rektum'),
												('A', 'Ascendens')])



	culture_cancer = StringField(u'Odling: Cancer', description=u'Scanna streckkod på rör')
	culture_cancer_loc = SelectField('', choices=[('C', 'Caekum'),
													('T', 'Transversum'),
													('D', 'Descendens'),
													('R', 'Rektum'),
													('A', 'Ascendens')])



	dna_close_cancer = StringField(u'DNA:Nära Cancer', description=u'Scanna streckkod på rör')
	dna_close_cancer_loc = SelectField('', choices=[('C', 'Caekum'),
													('T', 'Transversum'),
													('D', 'Descendens'),
													('R', 'Rektum'),
													('A', 'Ascendens')])



	culture_close_cancer = StringField(u'Odling:Nära Cancer', description=u'Scanna streckkod på rör')
	culture_close_cancer_loc = SelectField('', choices=[('C', 'Caekum'),
													('T', 'Transversum'),
													('D', 'Descendens'),
													('R', 'Rektum'),
													('A', 'Ascendens')])



	dna_close_diverticle = StringField(u'DNA:Nära Divertikel', description=u'Scanna streckkod på rör')
	dna_close_diverticle_loc = SelectField('', choices=[('C', 'Caekum'),
														('T', 'Transversum'),
														('D', 'Descendens'),
														('R', 'Rektum'),
														('A', 'Ascendens')])



	culture_close_diverticle = StringField(u'Odling:Nära Divertikel', description=u'Scanna streckkod på rör')
	culture_close_diverticle_loc = SelectField('', choices=[('C', 'Caekum'),
															('T', 'Transversum'),
															('D', 'Descendens'),
															('R', 'Rektum'),
															('A', 'Ascendens')])



	dna_ibd = StringField(u'DNA:IBD (inflammation)', description=u'Scanna streckkod på rör')
	dna_ibd_loc = SelectField('', choices=[('C', 'Caekum'),
											('T', 'Transversum'),
											('D', 'Descendens'),
											('R', 'Rektum'),
											('A', 'Ascendens')])



	culture_ibd = StringField(u'Odling:IBD (inflammation)', description=u'Scanna streckkod på rör')
	culture_ibd_loc = SelectField('', choices=[('C', 'Caekum'),
												('T', 'Transversum'),
												('D', 'Descendens'),
												('R', 'Rektum'),
												('A', 'Ascendens')])



	dna_close_ibd = StringField(u'DNA:Nära IBD', description=u'Scanna streckkod på rör')
	dna_close_ibd_loc = SelectField('', choices=[('C', 'Caekum'),
													('T', 'Transversum'),
													('D', 'Descendens'),
													('R', 'Rektum'),
													('A', 'Ascendens')])



	culture_close_ibd = StringField(u'ODL:Nära IBD', description=u'Scanna streckkod på rör')
	culture_close_ibd_loc = SelectField('', choices=[('C', 'Caekum'),
													('T', 'Transversum'),
													('D', 'Descendens'),
													('R', 'Rektum'),
													('A', 'Ascendens')])


	submit = SubmitField('Skicka')
