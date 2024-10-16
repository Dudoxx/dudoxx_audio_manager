from odoo import models, fields

class AccessControl(models.Model):
    _name = 'dudoxx.audio.access.control'
    _description = 'Access Control'

    name = fields.Char(string='Access Control Name', required=True)
    model_id = fields.Many2one('ir.model', string='Model', required=False)
    group_id = fields.Many2one('res.groups', string='User Group', required=True)
    permission_type = fields.Selection([
        ('read', 'Read'),
        ('write', 'Write'),
        ('create', 'Create'),
        ('delete', 'Delete')
    ], string='Permission Type', required=True)
