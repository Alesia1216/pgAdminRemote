# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class Car(models.Model):
    _name = 'odoo_model_advanced.car'
    _description = 'Coche'

    name = fields.Char(string='Modelo')
    number_plate = fields.Char(string='Matrícula')
    cv = fields.Float(string='CV')
    colour = fields.Char(string='Color')
    fuel_litres = fields.Float(string='Litros')
    is_new = fields.Boolean(string='Coche nuevo', default=True)
    car_type = fields.Selection(string='Tipo de coche')
    car_type = fields.Selection(
        selection=[
            ('coche_trabajo', 'Coche de trabajo'),
            ('coche_particular', 'Coche particular'),
            ('coche_alquiler', 'Coche de alquiler'),
        ],
        string='Estado',
    )
    description = fields.Text(string='Descripción')
    image = fields.Image(string='Imagen', max_width=1024, max_height=1024)




