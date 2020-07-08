from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    instructor = fields.Boolean("Instructor", default=False)

    session_ids = fields.Many2many('openacademy.session',
        string="Attended Sessions", readonly=True)
    channel     = fields.Char(string="Youtube ")
    # mobile       = fields.Char(string="mobile instructor" ,required=True)
    _sql_constraints=[
        ("mobile__unique","unique(mobile)","this mobile is already exist.")
    ]