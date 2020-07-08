from odoo import fields, models,_

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
    def make_new_session(self):
        self.ensure_one()
        context ={'defualt_instructor_id':self.ids,'defualt_seats':2}
        return {
            'name':_('new session'),
            'view_type':'form',
            'view_mode':'form',
            'res_model': 'openacademy.session',
            'view_id':self.env.ref( 'openacademy.session_form_view').id,
            'type': 'ir.actions.act_window',
            'target':'new',
            'context':context

        }