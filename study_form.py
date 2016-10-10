#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-

from flask import Flask, flash, render_template, session, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_script import Manager
from kolbibakt_form import MainForm
import pandas as pd
from collections import OrderedDict
from datetime import date

import excel_io
from config import XLS_FILE


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'secretkey'
manager = Manager(app)

def get_gender(personnummer):
	if int(str(personnummer)[-2]) % 2 == 0:
		return 'woman'
	else:
		return 'man'


def get_age(personnummer):
	dob_year = int(personnummer[0:4])
	dob_month = int(personnummer[4:6])
	dob_day = int(personnummer[6:8])
	today = date.today()
	return today.year - dob_year - ((today.month, today.day) < (dob_month, dob_day))


@app.route('/', methods=['GET', 'POST'])
def index():
	form = MainForm(csrf_enabled=False)



	if form.validate_on_submit():

		dd = OrderedDict()
		for field in form:
			if field.name not in ['submit', 'csrf_token']:
				if field.label.text:
					l_text = field.label.text
				else:
					l_text = field.name

				if field.name == 'snr':
					data = 'SR%03d' % field.data
				elif field.name in ['pnumber', 'asa']:
					data = int(field.data)
				else:
					data = field.data
				dd[l_text] = data

			dfd = pd.DataFrame(data=dd, index=[0])

		df = pd.DataFrame(data=OrderedDict([('ID_number', 'SR%03d' % form['snr'].data),
			('Personal_number', int(form['pnumber'].data)),
			('Gender', get_gender(form['pnumber'].data)),
			('Age', get_age(form['pnumber'].data)),
			('ASA', int(form['asa'].data)),
			('Earlier_colonscopy', form['earlier_col'].data),
			('Colonoscopy_reason', form['col_reason'].data),
			('Bowl_prep', form['bowl_prep'].data),
			('Full_colonoscopy', form['full_col'].data),
			('Feaces_culture', form['feac_culture'].data),
			('Main_diagnosis', form['main_diagnosis'].data)]), index=[0])


		excel_io.write_to_xlsfile(dfd, XLS_FILE)

		return redirect('/')

	return render_template('index.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)
