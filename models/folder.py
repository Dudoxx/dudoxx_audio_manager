from odoo import models, fields

class AudioFolder(models.Model):
    _name = 'dudoxx.audio.folder'
    _description = 'Audio Folder'

    name = fields.Char(string='Folder Name', required=True)
    parent_id = fields.Many2one('dudoxx.audio.folder', string='Parent Folder')
    child_ids = fields.One2many('dudoxx.audio.folder', 'parent_id', string='Subfolders')
    recording_ids = fields.One2many('dudoxx.audio.recording', 'folder_id', string='Recordings in Folder')
