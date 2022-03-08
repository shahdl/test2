from odoo import models, fields


class Plants(models.Model):
    _name = 'nursery.plant'

    name = fields.Char("Plant Name")
    price = fields.Float()


# class Customer(models.Model):
#     _name = 'nursery.customer'
#
#     name = fields.Char("Customer Name", required=True)
#     email = fields.Char(help="To receive the newsletter")
