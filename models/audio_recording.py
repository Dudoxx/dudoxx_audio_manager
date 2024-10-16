from odoo import models, fields

class AudioRecording(models.Model):
    _name = 'dudoxx.audio.recording'
    _description = 'Audio Recording'

    name = fields.Char(string='Recording Title', required=True)
    file = fields.Binary(string='Audio File')
    duration = fields.Float(string='Duration (seconds)')
    language_id = fields.Many2one('res.lang', string='Language')
    transcription = fields.Text(string='Transcription')
    translation_ids = fields.One2many('dudoxx.audio.translation', 'recording_id', string='Translations')
    chunk_ids = fields.One2many('dudoxx.audio.chunk', 'recording_id', string='Audio Chunks')
    folder_id = fields.Many2one('dudoxx.audio.folder', string='Folder')
    cloud_storage_url = fields.Char(string='Cloud Storage URL')
    status = fields.Selection([
        ('new', 'New'),
        ('transcribed', 'Transcribed'),
        ('translated', 'Translated'),
        ('updated', 'Updated')
    ], string='Status', default='new')
    owner_id = fields.Many2one('res.users', string='Owner')
    create_date = fields.Datetime(string='Date Added', readonly=True)
    write_date = fields.Datetime(string='Last Modified Date', readonly=True)
