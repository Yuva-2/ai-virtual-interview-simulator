* {
  box-sizing: border-box;
}

:root {
  --bg: #0b1120;
  --panel: #111827;
  --panel-soft: #1f2937;
  --card: #ffffff;
  --card-soft: #f8fafc;
  --primary: #5b8cff;
  --primary-strong: #3b82f6;
  --accent: #22c55e;
  --warning: #fbbf24;
  --danger: #f87171;
  --text: #e5eefb;
  --muted: #90a3bf;
  --border: rgba(148, 163, 184, 0.2);
  --shadow: 0 20px 40px rgba(15, 23, 42, 0.35);
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  min-height: 100vh;
  font-family: Inter, 'Segoe UI', sans-serif;
  background: radial-gradient(circle at top, #16213d 0%, var(--bg) 45%);
  color: var(--text);
}

button,
textarea,
select {
  font: inherit;
}

.app-shell {
  max-width: 1480px;
  margin: 0 auto;
  padding: 24px;
}

.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 22px;
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-mark {
  width: 42px;
  height: 42px;
  border-radius: 12px;
  background: linear-gradient(135deg, var(--primary), #8b5cf6);
  display: grid;
  place-items: center;
  font-weight: 700;
  color: white;
  box-shadow: var(--shadow);
}

.brand h1 {
  margin: 0;
  font-size: 1.15rem;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(59, 130, 246, 0.12);
  color: #cfe1ff;
  border: 1px solid rgba(96, 165, 250, 0.25);
  border-radius: 999px;
  padding: 7px 12px;
  font-size: 0.8rem;
}

.dashboard {
  display: grid;
  grid-template-columns: 380px 1fr 360px;
  gap: 20px;
}

.panel {
  background: rgba(17, 24, 39, 0.88);
  border: 1px solid var(--border);
  border-radius: 20px;
  box-shadow: var(--shadow);
}

.side-panel,
.report-panel {
  padding: 20px;
}

.main-panel {
  padding: 20px;
}

.section-label {
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--muted);
  font-size: 0.72rem;
  margin-bottom: 12px;
}

.job-card {
  background: linear-gradient(135deg, rgba(91, 140, 255, 0.15), rgba(139, 92, 246, 0.1));
  border: 1px solid rgba(91, 140, 255, 0.25);
  border-radius: 16px;
  padding: 18px;
  margin-bottom: 18px;
}

.job-card h2,
.profile-card h2,
.report-panel h3,
.main-panel h2 {
  margin-top: 0;
}

.meta-list {
  display: grid;
  gap: 12px;
  margin: 18px 0;
}

.meta-item {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  color: var(--muted);
  font-size: 0.92rem;
}

.meta-item strong {
  color: var(--text);
}

.profile-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 18px;
  margin-bottom: 18px;
}

.avatar-row {
  display: flex;
  gap: 12px;
  align-items: center;
  margin-bottom: 14px;
}

.avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: linear-gradient(135deg, #34d399, #3b82f6);
  display: grid;
  place-items: center;
  font-weight: 700;
}

.chip-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 14px;
}

.chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 10px;
  background: rgba(34, 197, 94, 0.1);
  color: #d7fbe5;
  border: 1px solid rgba(34, 197, 94, 0.2);
  border-radius: 999px;
  font-size: 0.78rem;
}

.main-panel {
  min-height: 760px;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  margin-bottom: 18px;
}

.primary-button,
.secondary-button {
  border: none;
  border-radius: 12px;
  padding: 11px 16px;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s ease, opacity 0.2s ease;
}

.primary-button {
  background: linear-gradient(135deg, var(--primary), #8b5cf6);
  color: white;
}

.secondary-button {
  background: rgba(148, 163, 184, 0.12);
  color: var(--text);
  border: 1px solid rgba(148, 163, 184, 0.2);
}

.primary-button:hover,
.secondary-button:hover {
  transform: translateY(-1px);
}

.question-list {
  display: grid;
  gap: 18px;
}

.question-card {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 18px;
}

.question-header {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  align-items: flex-start;
  margin-bottom: 12px;
}

.question-tag {
  padding: 7px 10px;
  background: rgba(91, 140, 255, 0.1);
  color: #cfe1ff;
  border-radius: 999px;
  border: 1px solid rgba(91, 140, 255, 0.25);
  font-size: 0.72rem;
}

.question-card h3 {
  margin: 0;
  font-size: 1.05rem;
}

.answer-box {
  width: 100%;
  min-height: 120px;
  border: 1px solid rgba(148, 163, 184, 0.3);
  border-radius: 14px;
  background: rgba(15, 23, 42, 0.7);
  color: var(--text);
  padding: 14px 16px;
  resize: vertical;
  outline: none;
}

.answer-box:focus {
  border-color: rgba(96, 165, 250, 0.8);
  box-shadow: 0 0 0 4px rgba(96, 165, 250, 0.12);
}

.score-ring {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-weight: 700;
  color: white;
  background: conic-gradient(var(--accent) 0deg 280deg, rgba(255, 255, 255, 0.1) 0deg 360deg);
  position: relative;
  margin: 0 auto 12px auto;
}

.score-ring::after {
  content: '';
  position: absolute;
  inset: 12px;
  border-radius: 50%;
  background: rgba(15, 23, 42, 0.96);
}

.score-ring span {
  position: relative;
  z-index: 1;
  font-size: 1.3rem;
}

.result-box {
  background: rgba(15, 23, 42, 0.72);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 16px;
  margin-top: 18px;
}

.result-box h4 {
  margin-top: 0;
}

.summary-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
  margin-top: 12px;
}

.summary-card {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(148, 163, 184, 0.18);
  border-radius: 12px;
  padding: 12px;
}

.summary-card strong {
  display: block;
  font-size: 1.3rem;
  margin-bottom: 6px;
}

.list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 10px;
}

.list li {
  padding: 10px 12px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(148, 163, 184, 0.14);
  line-height: 1.5;
}

@media (max-width: 1100px) {
  .dashboard {
    grid-template-columns: 1fr;
  }

  .report-panel {
    order: 3;
  }
}
