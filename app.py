#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template_string, request, jsonify, send_file
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, quote
import os
import re
from pathlib import Path
import time
import hashlib
import random
import json
import sys
import traceback

app = Flask(__name__)

# ULTIMATE VIP HTML TEMPLATE
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>⚡ ANSH WEB CLONER ⚡ - Powerfull Bot Bypass</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: #000000;
            font-family: 'Orbitron', monospace;
            min-height: 100vh;
            overflow-x: hidden;
        }
        
        /* Animated Background */
        .bg-animation {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            background: radial-gradient(circle at center, #001100 0%, #000000 100%);
        }
        
        .bg-animation::before {
            content: '';
            position: absolute;
            width: 200%;
            height: 200%;
            top: -50%;
            left: -50%;
            background: repeating-linear-gradient(
                0deg,
                transparent,
                transparent 2px,
                rgba(0, 255, 0, 0.03) 2px,
                rgba(0, 255, 0, 0.03) 4px
            );
            animation: scan 10s linear infinite;
        }
        
        @keyframes scan {
            0% { transform: translateY(0); }
            100% { transform: translateY(20px); }
        }
        
        .container {
            position: relative;
            z-index: 10;
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        
        /* Glitch Header */
        .glitch-header {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .glitch {
            font-size: 4rem;
            font-weight: 900;
            position: relative;
            text-shadow: 0.05em 0 0 rgba(255,0,0,0.75), -0.05em -0.025em 0 rgba(0,255,0,0.75);
            animation: glitch-skew 3s infinite;
        }
        
        .glitch span {
            background: linear-gradient(135deg, #ff0066, #ff00cc, #00ffcc, #ff0066);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            animation: gradient 3s ease infinite;
        }
        
        @keyframes glitch-skew {
            0%, 100% { transform: skew(0deg, 0deg); }
            95% { transform: skew(0deg, 0deg); }
            96% { transform: skew(2deg, 1deg); }
            97% { transform: skew(-2deg, -1deg); }
            98% { transform: skew(1deg, 2deg); }
            99% { transform: skew(-1deg, -2deg); }
        }
        
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .subtitle {
            text-align: center;
            color: #00ffcc;
            font-size: 1rem;
            letter-spacing: 3px;
            margin-top: 10px;
        }
        
        /* VIP Card */
        .vip-card {
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            border: 1px solid rgba(0, 255, 204, 0.3);
            padding: 35px;
            margin-bottom: 30px;
            transition: all 0.3s;
        }
        
        .vip-card:hover {
            border-color: #ff0066;
            box-shadow: 0 0 40px rgba(255, 0, 102, 0.2);
        }
        
        /* Input Styles */
        .input-wrapper {
            margin-bottom: 25px;
        }
        
        .input-label {
            display: block;
            color: #00ffcc;
            margin-bottom: 10px;
            font-size: 1rem;
            font-weight: bold;
        }
        
        .neon-input {
            width: 100%;
            padding: 15px;
            background: #0a0a0a;
            border: 2px solid #ff0066;
            border-radius: 12px;
            color: #00ffcc;
            font-size: 1rem;
            font-family: monospace;
            transition: all 0.3s;
        }
        
        .neon-input:focus {
            outline: none;
            border-color: #00ffcc;
            box-shadow: 0 0 20px rgba(0, 255, 204, 0.3);
        }
        
        /* Method Grid */
        .method-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 12px;
            margin-bottom: 25px;
        }
        
        .method-item {
            background: rgba(0, 255, 204, 0.05);
            border: 1px solid #00ffcc;
            border-radius: 10px;
            padding: 12px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .method-item.selected {
            background: linear-gradient(135deg, #ff0066, #00ffcc);
            border-color: transparent;
        }
        
        .method-item input {
            margin-right: 8px;
        }
        
        /* Button */
        .clone-btn {
            width: 100%;
            padding: 18px;
            background: linear-gradient(135deg, #ff0066, #cc0033);
            border: none;
            border-radius: 12px;
            color: white;
            font-size: 1.3rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            text-transform: uppercase;
            letter-spacing: 3px;
            font-family: monospace;
        }
        
        .clone-btn:hover {
            transform: scale(1.02);
            box-shadow: 0 0 30px rgba(255, 0, 102, 0.6);
        }
        
        /* Terminal */
        .terminal-window {
            background: #000000;
            border: 2px solid #00ffcc;
            border-radius: 15px;
            overflow: hidden;
        }
        
        .terminal-header {
            background: #0a0a0a;
            padding: 12px 20px;
            border-bottom: 1px solid #00ffcc;
            display: flex;
            gap: 10px;
        }
        
        .term-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }
        .term-dot:nth-child(1) { background: #ff0066; }
        .term-dot:nth-child(2) { background: #00ffcc; }
        .term-dot:nth-child(3) { background: #00ff66; }
        
        .terminal-content {
            padding: 20px;
            min-height: 450px;
            max-height: 550px;
            overflow-y: auto;
            font-family: monospace;
        }
        
        .term-line {
            color: #00ffcc;
            margin: 6px 0;
            font-size: 0.85rem;
            white-space: pre-wrap;
        }
        
        .term-prompt {
            color: #ff0066;
        }
        
        /* Result Section */
        .result-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .file-section {
            background: #0a0a0a;
            border-radius: 10px;
            padding: 15px;
        }
        
        .file-section h4 {
            color: #ff0066;
            margin-bottom: 10px;
            border-bottom: 1px solid #00ffcc;
            padding-bottom: 5px;
        }
        
        .file-list {
            max-height: 300px;
            overflow-y: auto;
        }
        
        .file-item {
            color: #00ffcc;
            padding: 8px;
            border-bottom: 1px solid #1a1a1a;
            cursor: pointer;
            font-size: 0.8rem;
        }
        
        .file-item:hover {
            background: rgba(0, 255, 204, 0.1);
        }
        
        /* Modal */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.98);
            z-index: 1000;
        }
        
        .modal-content {
            position: relative;
            background: #0a0a0a;
            margin: 50px auto;
            width: 90%;
            max-width: 1200px;
            border: 2px solid #00ffcc;
            border-radius: 15px;
            padding: 20px;
        }
        
        .modal-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #00ffcc;
        }
        
        .close {
            color: #ff0066;
            font-size: 28px;
            cursor: pointer;
        }
        
        .code-view {
            background: #000;
            padding: 15px;
            border-radius: 10px;
            max-height: 500px;
            overflow: auto;
        }
        
        .code-view pre {
            color: #00ffcc;
            font-family: monospace;
            font-size: 0.8rem;
            white-space: pre-wrap;
        }
        
        @media (max-width: 768px) {
            .glitch { font-size: 2rem; }
            .vip-card { padding: 20px; }
            .term-line { font-size: 0.7rem; }
        }
    </style>
</head>
<body>
    <div class="bg-animation"></div>
    
    <div class="container">
        <div class="glitch-header">
            <div class="glitch">
                <span>◢ ANSH WEB CLONER ◣</span>
            </div>
            <div class="subtitle">⚡ POWERFULL BOT BYPASS EDITION ⚡</div>
        </div>
        
        <div class="vip-card">
            <div class="input-wrapper">
                <label class="input-label">🎯 TARGET WEBSITE URL</label>
                <input type="text" id="targetUrl" class="neon-input" placeholder="https://example.com" value="https://httpbin.org/html">
            </div>
            
            <label class="input-label">🛡️ BYPASS METHOD</label>
            <div class="method-grid" id="methodGrid">
                <div class="method-item" data-method="auto">
                    <input type="radio" name="bypass" value="auto" checked> 🤖 AUTO DETECT
                </div>
                <div class="method-item" data-method="direct">
                    <input type="radio" name="bypass" value="direct"> ⚡ DIRECT FETCH
                </div>
                <div class="method-item" data-method="stealth">
                    <input type="radio" name="bypass" value="stealth"> 🎭 STEALTH MODE
                </div>
                <div class="method-item" data-method="retry">
                    <input type="radio" name="bypass" value="retry"> 🔄 RETRY ENGINE
                </div>
            </div>
            
            <div class="input-wrapper">
                <label class="input-label">⚙️ CLONING OPTIONS</label>
                <div class="method-grid">
                    <div class="method-item">
                        <input type="checkbox" id="onlyCode" checked> 💻 ONLY CODE
                    </div>
                    <div class="method-item">
                        <input type="checkbox" id="fixLinks" checked> 🔗 FIX LINKS
                    </div>
                    <div class="method-item">
                        <input type="checkbox" id="deepExtract" checked> 🔍 DEEP EXTRACT
                    </div>
                </div>
            </div>
            
            <button class="clone-btn" onclick="startCloning()">🚀 START CLONING NOW 🚀</button>
        </div>
        
        <div class="vip-card">
            <div class="terminal-window">
                <div class="terminal-header">
                    <div class="term-dot"></div>
                    <div class="term-dot"></div>
                    <div class="term-dot"></div>
                    <span style="color: #00ffcc; margin-left: 10px;">TERMINAL OUTPUT</span>
                </div>
                <div class="terminal-content" id="terminal">
                    <div class="term-line"><span class="term-prompt">$></span> ANSH WEB CLONER INITIALIZED</div>
                    <div class="term-line"><span class="term-prompt">$></span> READY TO CLONE</div>
                </div>
            </div>
        </div>
        
        <div class="vip-card" id="resultCard" style="display: none;">
            <label class="input-label">📁 CLONED FILES STRUCTURE</label>
            <div id="resultContent"></div>
        </div>
    </div>
    
    <div id="modal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 style="color: #00ffcc;">📄 FILE CONTENT</h3>
                <span class="close" onclick="closeModal()">&times;</span>
            </div>
            <div class="code-view">
                <pre id="codeContent">Loading...</pre>
            </div>
        </div>
    </div>
    
    <script>
        // Method selection
        document.querySelectorAll('.method-item').forEach(item => {
            item.addEventListener('click', function(e) {
                const radio = this.querySelector('input[type="radio"]');
                if (radio) {
                    radio.checked = true;
                    document.querySelectorAll('.method-item').forEach(m => m.classList.remove('selected'));
                    this.classList.add('selected');
                }
            });
        });
        
        function addTerminalLine(text, type = 'info') {
            const terminal = document.getElementById('terminal');
            const line = document.createElement('div');
            line.className = 'term-line';
            line.innerHTML = `<span class="term-prompt">$></span> ${text}`;
            terminal.appendChild(line);
            terminal.scrollTop = terminal.scrollHeight;
        }
        
        function updateProgress(percent, message) {
            const barLen = 30;
            const filled = Math.floor(percent / (100 / barLen));
            const bar = '█'.repeat(filled) + '░'.repeat(barLen - filled);
            addTerminalLine(`[${bar}] ${percent}% - ${message}`);
        }
        
        async function startCloning() {
            const url = document.getElementById('targetUrl').value;
            const bypassMethod = document.querySelector('input[name="bypass"]:checked').value;
            const onlyCode = document.getElementById('onlyCode').checked;
            const fixLinks = document.getElementById('fixLinks').checked;
            const deepExtract = document.getElementById('deepExtract').checked;
            
            if (!url) {
                addTerminalLine('❌ ERROR: Please enter a valid URL');
                return;
            }
            
            document.getElementById('terminal').innerHTML = '';
            
            addTerminalLine('╔═══════════════════════════════════════════════════════════════╗');
            addTerminalLine('║  🔥 ANSH WEB CLONER ACTIVATED 🔥                         ║');
            addTerminalLine(`║  🎯 TARGET: ${url.substring(0, 50)}${url.length > 50 ? '...' : ''}`);
            addTerminalLine(`║  🛡️ BYPASS: ${bypassMethod.toUpperCase()}`);
            addTerminalLine(`║  💻 MODE: ${onlyCode ? 'CODE ONLY' : 'FULL CLONE'}`);
            addTerminalLine('╚═══════════════════════════════════════════════════════════════╝');
            
            updateProgress(0, 'Initializing cloning engine...');
            await sleep(500);
            updateProgress(10, 'Setting up bypass methods...');
            await sleep(600);
            updateProgress(25, 'Connecting to target server...');
            await sleep(800);
            updateProgress(40, 'Fetching HTML content...');
            await sleep(500);
            updateProgress(60, 'Extracting CSS & JS resources...');
            await sleep(700);
            updateProgress(80, 'Processing and saving files...');
            
            try {
                const response = await fetch('/api/clone', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        url: url,
                        bypass_method: bypassMethod,
                        only_code: onlyCode,
                        fix_links: fixLinks,
                        deep_extract: deepExtract
                    })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    updateProgress(100, '✅ CLONING COMPLETE!');
                    addTerminalLine('');
                    addTerminalLine(`✅ SAVED TO: ${data.save_path}`);
                    addTerminalLine(`📁 TOTAL FILES: ${data.total_files}`);
                    addTerminalLine(`📄 HTML: ${data.html} | CSS: ${data.css} | JS: ${data.js}`);
                    addTerminalLine('🎉 Website cloned successfully!');
                    
                    document.getElementById('resultCard').style.display = 'block';
                    displayFiles(data.files);
                } else {
                    updateProgress(0, '❌ CLONING FAILED');
                    addTerminalLine(`❌ ERROR: ${data.error}`);
                }
            } catch (error) {
                addTerminalLine(`❌ ERROR: ${error.message}`);
            }
        }
        
        function displayFiles(files) {
            let html = '<div class="result-grid">';
            
            const types = {
                'html': 'HTML FILES',
                'css': 'CSS FILES', 
                'js': 'JAVASCRIPT FILES'
            };
            
            for (const [type, title] of Object.entries(types)) {
                const typeFiles = files.filter(f => f.type === type);
                if (typeFiles.length > 0) {
                    html += `
                        <div class="file-section">
                            <h4>📁 ${title}</h4>
                            <div class="file-list">
                                ${typeFiles.map(f => `<div class="file-item" onclick="viewCode('${f.path}')">📄 ${f.name}</div>`).join('')}
                            </div>
                        </div>
                    `;
                }
            }
            
            html += '</div>';
            document.getElementById('resultContent').innerHTML = html;
        }
        
        async function viewCode(path) {
            const modal = document.getElementById('modal');
            const codeContent = document.getElementById('codeContent');
            modal.style.display = 'block';
            codeContent.textContent = 'Loading file content...';
            
            try {
                const response = await fetch(`/api/view?path=${encodeURIComponent(path)}`);
                const data = await response.json();
                codeContent.textContent = data.content;
            } catch (error) {
                codeContent.textContent = `Error: ${error.message}`;
            }
        }
        
        function closeModal() {
            document.getElementById('modal').style.display = 'none';
        }
        
        function sleep(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        }
        
        // Close modal on escape
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                closeModal();
            }
        });
    </script>
</body>
</html>
'''

class PowerfullWebCloner:
    def __init__(self, target_url, base_path="/storage/emulated/0/NIROB-WEB-COPY"):
        self.target_url = target_url
        self.domain = urlparse(target_url).netloc.replace('.', '_').replace('-', '_')
        self.base_path = Path(base_path) / self.domain
        self.downloaded = set()
        self.files = []
        self.stats = {'html': 0, 'css': 0, 'js': 0}
        
    def create_session(self, method='auto'):
        """Create session with multiple bypass attempts"""
        session = requests.Session()
        
        # Multiple user agents
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Version/17.0 Mobile/15E148 Safari/604.1'
        ]
        
        session.headers.update({
            'User-Agent': random.choice(user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'DNT': '1'
        })
        
        # Disable SSL verification
        session.verify = False
        
        return session
    
    def fetch_with_retry(self, url, session, max_retries=3):
        """Fetch URL with retry logic"""
        for attempt in range(max_retries):
            try:
                # Add random delay between retries
                if attempt > 0:
                    time.sleep(1 * attempt)
                
                response = session.get(url, timeout=30)
                if response.status_code == 200:
                    return response.text
                elif response.status_code == 403:
                    # Try with different headers
                    session.headers['User-Agent'] = random.choice([
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
                        'curl/7.68.0'
                    ])
                    continue
            except Exception as e:
                if attempt == max_retries - 1:
                    raise e
                continue
        return None
    
    def extract_resources(self, html, base_url):
        """Extract all CSS and JS resources from HTML"""
        soup = BeautifulSoup(html, 'html.parser')
        resources = {'css': [], 'js': []}
        
        # Extract CSS files
        for link in soup.find_all('link', rel='stylesheet'):
            href = link.get('href')
            if href:
                full_url = urljoin(base_url, href)
                if not full_url.startswith('data:'):
                    resources['css'].append(full_url)
        
        # Extract JS files
        for script in soup.find_all('script', src=True):
            src = script.get('src')
            if src:
                full_url = urljoin(base_url, src)
                if not full_url.startswith('data:'):
                    resources['js'].append(full_url)
        
        # Extract inline styles
        style_tags = soup.find_all('style')
        for idx, style in enumerate(style_tags):
            if style.string:
                inline_css = style.string
                css_path = self.base_path / 'css' / f'inline_{idx}.css'
                with open(css_path, 'w', encoding='utf-8') as f:
                    f.write(inline_css)
                self.stats['css'] += 1
                self.files.append({'name': f'inline_{idx}.css', 'path': str(css_path), 'type': 'css'})
        
        # Extract inline scripts
        script_tags = soup.find_all('script', src=False)
        for idx, script in enumerate(script_tags):
            if script.string:
                inline_js = script.string
                js_path = self.base_path / 'js' / f'inline_{idx}.js'
                with open(js_path, 'w', encoding='utf-8') as f:
                    f.write(inline_js)
                self.stats['js'] += 1
                self.files.append({'name': f'inline_{idx}.js', 'path': str(js_path), 'type': 'js'})
        
        return resources
    
    def download_resource(self, url, session, resource_type):
        """Download a single resource"""
        try:
            content = self.fetch_with_retry(url, session)
            if content:
                # Determine filename
                parsed = urlparse(url)
                filename = Path(parsed.path).name
                if not filename or '.' not in filename:
                    filename = f"{resource_type}_{hashlib.md5(url.encode()).hexdigest()[:8]}.{resource_type}"
                
                # Sanitize filename
                filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
                if resource_type == 'css' and not filename.endswith('.css'):
                    filename += '.css'
                elif resource_type == 'js' and not filename.endswith('.js'):
                    filename += '.js'
                
                save_path = self.base_path / resource_type / filename
                save_path.parent.mkdir(parents=True, exist_ok=True)
                
                with open(save_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.stats[resource_type] += 1
                self.files.append({'name': filename, 'path': str(save_path), 'type': resource_type})
                return True
        except Exception as e:
            print(f"Error downloading {url}: {e}")
        return False
    
    def clone(self, bypass_method='auto', only_code=True, fix_links=True, deep_extract=True):
        """Main clone function"""
        try:
            # Create directories
            self.base_path.mkdir(parents=True, exist_ok=True)
            (self.base_path / 'css').mkdir(exist_ok=True)
            (self.base_path / 'js').mkdir(exist_ok=True)
            
            # Create session
            session = self.create_session(bypass_method)
            
            # Fetch main page
            html = self.fetch_with_retry(self.target_url, session)
            
            if not html:
                return False, "Failed to fetch website. The site might have bot protection or be unreachable."
            
            # Save main HTML
            html_path = self.base_path / 'index.html'
            with open(html_path, 'w', encoding='utf-8') as f:
                if fix_links:
                    # Fix relative links
                    soup = BeautifulSoup(html, 'html.parser')
                    for link in soup.find_all(['link', 'script']):
                        if link.get('href') and 'css' in link.get('href', ''):
                            link['href'] = f"css/{Path(link['href']).name}"
                        if link.get('src') and 'js' in link.get('src', ''):
                            link['src'] = f"js/{Path(link['src']).name}"
                    html = str(soup)
                f.write(html)
            
            self.stats['html'] += 1
            self.files.append({'name': 'index.html', 'path': str(html_path), 'type': 'html'})
            
            # Extract and download resources
            if deep_extract:
                resources = self.extract_resources(html, self.target_url)
                
                # Download CSS files
                for css_url in resources['css'][:30]:  # Limit to 30 files
                    self.download_resource(css_url, session, 'css')
                
                # Download JS files
                for js_url in resources['js'][:30]:  # Limit to 30 files
                    self.download_resource(js_url, session, 'js')
            
            total = sum(self.stats.values())
            return True, {
                'save_path': str(self.base_path),
                'total_files': total,
                'html': self.stats['html'],
                'css': self.stats['css'],
                'js': self.stats['js'],
                'files': self.files
            }
            
        except Exception as e:
            return False, str(e)

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/clone', methods=['POST'])
def clone():
    data = request.json
    target_url = data.get('url')
    bypass_method = data.get('bypass_method', 'auto')
    only_code = data.get('only_code', True)
    fix_links = data.get('fix_links', True)
    deep_extract = data.get('deep_extract', True)
    
    if not target_url:
        return jsonify({'success': False, 'error': 'URL is required'})
    
    # Add scheme if missing
    if not target_url.startswith(('http://', 'https://')):
        target_url = 'https://' + target_url
    
    cloner = PowerfullWebCloner(target_url)
    success, result = cloner.clone(bypass_method, only_code, fix_links, deep_extract)
    
    if success:
        return jsonify({'success': True, **result})
    else:
        return jsonify({'success': False, 'error': result})

@app.route('/api/view', methods=['GET'])
def view_file():
    file_path = request.args.get('path')
    if not file_path:
        return jsonify({'content': 'No file path provided'})
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return jsonify({'content': content})
    except Exception as e:
        return jsonify({'content': f'Error reading file: {str(e)}'})

if __name__ == '__main__':
    # Disable SSL warnings
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    print("""
    ╔══════════════════════════════════════════════════════════════════╗
    ║                                                                  ║
    ║    ███╗   ██╗██╗██████╗  ██████╗ ██████╗                         ║
    ║    ████╗  ██║██║██╔══██╗██╔═══██╗██╔══██╗                        ║
    ║    ██╔██╗ ██║██║██████╔╝██║   ██║██████╔╝                        ║
    ║    ██║╚██╗██║██║██╔══██╗██║   ██║██╔══██╗                        ║
    ║    ██║ ╚████║██║██║  ██║╚██████╔╝██████╔╝                        ║
    ║    ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝                         ║
    ║                                                                  ║
    ║              ⚡ POWERFULL BOT BYPASS EDITION ⚡                   ║
    ║                                                                  ║
    ║         🚀 SERVER: http://localhost:5000                        ║
    ║         📱 MOBILE: http://YOUR_IP:5000                          ║
    ║                                                                  ║
    ║         ✅ READY TO CLONE ANY WEBSITE                           ║
    ║         🔥 BOT BYPASS ACTIVE                                    ║
    ║                                                                  ║
    ╚══════════════════════════════════════════════════════════════════╝
    """)
    
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
