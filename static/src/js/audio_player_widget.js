/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState, useRef, onWillUpdateProps } from "@odoo/owl";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { useService } from "@web/core/utils/hooks";

export class AudioPlayerWidget extends Component {
    setup() {
        this.orm = useService("orm");
        this.audioElement = useRef('audioElement');

        this.state = useState({
            isPlaying: false,
            dataUrl: '',
            currentTime: 0,
            duration: 0,
            progress: 0,
        });

        // Process audio data only if value is a string
        if (typeof this.props.value === 'string') {
            this.processAudioData(this.props.value);
        }

        // Watch for changes in props to reset the audio status for new or updated records
        onWillUpdateProps((nextProps) => {
            if (nextProps.value !== this.props.value) {
                this.resetAudioPlayer();
                if (typeof nextProps.value === 'string') {
                    this.processAudioData(nextProps.value);
                }
            }
        });
    }

    async processAudioData(value) {
        if (typeof value !== 'string') {
            console.warn("AudioPlayerWidget - Invalid value type; expected string but received:", typeof value);
            return;
        }

        if (value.includes(' Mb')) {
            console.log("AudioPlayerWidget - Received file size, fetching actual data.");
            await this.fetchAudioData();
        } else if (value.length > 100) {
            this.state.dataUrl = `data:audio/mp3;base64,${value}`;
            console.log("AudioPlayerWidget - Valid base64 data found. dataUrl created.");
        } else {
            console.warn("AudioPlayerWidget - Invalid or missing audio data. Received:", value);
        }
    }

    async fetchAudioData() {
        try {
            const result = await this.orm.call(
                this.props.record.resModel,
                'read',
                [[this.props.record.resId], ['file']],
                { context: this.props.record.context }
            );
            if (result && result.length > 0 && result[0].file) {
                this.state.dataUrl = `data:audio/mp3;base64,${result[0].file}`;
                console.log("AudioPlayerWidget - Audio data fetched successfully.");
            } else {
                console.warn("AudioPlayerWidget - No audio data found after fetching.");
            }
        } catch (error) {
            console.error("AudioPlayerWidget - Error fetching audio data:", error);
        }
    }

    play() {
        if (this.audioElement.el) {
            this.audioElement.el.play().catch(error => {
                console.error("AudioPlayerWidget - Error playing audio:", error.message);
            });
            this.state.isPlaying = true;
            this.toggleVibratingBars(true);
        }
    }

    pause() {
        if (this.audioElement.el) {
            this.audioElement.el.pause();
            this.state.isPlaying = false;
            this.toggleVibratingBars(false);
        }
    }

    stop() {
        if (this.audioElement.el) {
            this.audioElement.el.pause();
            this.audioElement.el.currentTime = 0;
            this.state.isPlaying = false;
            this.toggleVibratingBars(false);
            this.updateProgress();
        }
    }

    updateProgress() {
        if (this.audioElement.el) {
            this.state.currentTime = this.audioElement.el.currentTime;
            this.state.progress = (this.state.currentTime / this.state.duration) * 100 || 0;
        }
    }

    setDuration() {
        if (this.audioElement.el) {
            this.state.duration = this.audioElement.el.duration;
        }
    }

    toggleVibratingBars(isActive) {
        const bars = document.querySelector(".vibrating-bars");
        if (bars) {
            bars.classList.toggle("active", isActive);
        }
    }

    formatTime(time) {
        const minutes = Math.floor(time / 60);
        const seconds = Math.floor(time % 60);
        return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }

    onProgressBarClick(event) {
        if (this.audioElement.el) {
            const progressBar = event.target;
            const clickPosition = event.clientX - progressBar.getBoundingClientRect().left;
            const clickPercentage = clickPosition / progressBar.offsetWidth;
            this.audioElement.el.currentTime = clickPercentage * this.state.duration;
            this.updateProgress();
        }
    }

    resetAudioPlayer() {
        if (this.audioElement.el) {
            this.audioElement.el.pause();
            this.audioElement.el.currentTime = 0;
        }
        this.state.isPlaying = false;
        this.state.dataUrl = '';
        this.state.currentTime = 0;
        this.state.duration = 0;
        this.state.progress = 0;
        console.log("AudioPlayerWidget - Audio player reset due to new or updated record.");
    }
}

AudioPlayerWidget.template = "dudoxx_audio_manager.AudioPlayerWidget";
AudioPlayerWidget.props = {
    ...standardFieldProps,
    value: { type: String, optional: true },
};

registry.category("fields").add("audio_player", AudioPlayerWidget);
