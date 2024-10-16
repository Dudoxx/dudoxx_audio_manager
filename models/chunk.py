from odoo import models, fields

class AudioChunk(models.Model):
    _name = 'dudoxx.audio.chunk'
    _description = 'Audio Chunk'

    recording_id = fields.Many2one('dudoxx.audio.recording', string='Related Audio Recording')
    start_time = fields.Float(string='Start Time (seconds)')
    end_time = fields.Float(string='End Time (seconds)')
    chunk_file = fields.Binary(string='Chunked Audio File')
    transcription = fields.Text(string='Transcription of the Chunk')
