import json

with open("combined_lavers_maun_dataset.json", "r", encoding="utf-8") as f:
    timber_data = json.load(f)

json_data_str = json.dumps(timber_data, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Strength Properties of Timber - BRE Interactive Explorer & Visualizer</title>
  <meta name="description" content="Interactive filterable dataset and graphical visualizer for mechanical and physical properties of timber species from BRE Reports (Lavers 1983 & Maun 1997 Supplement).">
  
  <!-- Work Sans Google Font -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Chart.js for Graphical Visualizer -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <style>
    :root {{
      --bg-color: #09090b;
      --card-bg: #141417;
      --card-border: #27272a;
      --text-main: #f4f4f5;
      --text-muted: #a1a1aa;
      --accent-orange: rgb(255, 140, 0); /* #ff8c00 */
      --accent-orange-bright: rgb(255, 140, 0);
      --accent-orange-glow: rgba(255, 140, 0, 0.25);
      --radius-lg: 12px;
      --radius-md: 8px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Work Sans', sans-serif;
      font-weight: 300; /* Work Sans Light */
      background-color: var(--bg-color);
      color: var(--text-main);
      min-height: 100vh;
      padding: 1.5rem 2rem;
      line-height: 1.6;
    }}

    .container {{
      max-width: 98vw;
      margin: 0 auto;
    }}

    /* Typography: Work Sans Regular for Headings & Titles */
    h1, h2, h3, h4, h5, h6, .heading-title {{
      font-family: 'Work Sans', sans-serif;
      font-weight: 400; /* Work Sans Regular */
      color: var(--text-main);
    }}

    /* Header */
    header {{
      text-align: center;
      margin-bottom: 1.5rem;
    }}

    .badge-top {{
      display: inline-block;
      padding: 0.35rem 1rem;
      background: rgba(255, 140, 0, 0.1);
      border: 1px solid rgba(255, 140, 0, 0.3);
      color: var(--accent-orange);
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 500;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      margin-bottom: 0.75rem;
    }}

    h1 {{
      font-size: 2.6rem;
      color: var(--accent-orange); /* Orange Highlight for Main Heading */
      letter-spacing: -0.02em;
      margin-bottom: 0.4rem;
    }}

    .subtitle {{
      color: var(--text-muted);
      font-size: 1.05rem;
      font-weight: 300;
    }}

    /* Intro / About Data Card */
    .about-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-left: 4px solid var(--accent-orange);
      border-radius: var(--radius-lg);
      padding: 1.25rem 1.75rem;
      margin-bottom: 1.75rem;
    }}

    .about-title {{
      font-size: 1.15rem;
      color: var(--accent-orange);
      font-weight: 400;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .about-text {{
      font-size: 0.92rem;
      color: #d4d4d8;
      font-weight: 300;
      line-height: 1.6;
    }}

    .sources-list {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1rem;
      margin-top: 0.75rem;
    }}

    .source-box {{
      background: #09090b;
      border: 1px solid #27272a;
      border-radius: var(--radius-md);
      padding: 0.85rem 1rem;
    }}

    .source-name {{
      font-weight: 400;
      color: #ffffff;
      font-size: 0.9rem;
      margin-bottom: 0.2rem;
    }}

    .source-desc {{
      font-size: 0.82rem;
      color: var(--text-muted);
      font-weight: 300;
    }}

    .source-link {{
      color: var(--accent-orange);
      text-decoration: none;
      font-weight: 400;
      transition: opacity 0.2s;
    }}

    .source-link:hover {{
      text-decoration: underline;
      opacity: 0.85;
    }}

    /* View Switcher Tabs */
    .tabs-nav {{
      display: flex;
      justify-content: center;
      gap: 1rem;
      margin-bottom: 1.75rem;
    }}

    .tab-btn {{
      padding: 0.65rem 1.5rem;
      background: #18181b;
      border: 1px solid var(--card-border);
      border-radius: 9999px;
      color: var(--text-muted);
      font-family: 'Work Sans', sans-serif;
      font-size: 0.95rem;
      font-weight: 400;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .tab-btn:hover {{
      color: var(--text-main);
      border-color: #3f3f46;
    }}

    .tab-btn.active {{
      background: var(--accent-orange);
      color: #000000;
      font-weight: 600;
      border-color: var(--accent-orange);
      box-shadow: 0 0 20px var(--accent-orange-glow);
    }}

    /* Summary Stats Grid - 3 Cards */
    .stats-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 1.25rem;
      margin-bottom: 1.5rem;
    }}

    .stat-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      padding: 1.25rem 1.5rem;
      transition: transform 0.2s ease, border-color 0.2s ease;
    }}

    .stat-card:hover {{
      border-color: rgba(255, 140, 0, 0.4);
    }}

    .stat-label {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 0.25rem;
      font-weight: 300;
    }}

    .stat-value {{
      font-family: 'Work Sans', sans-serif;
      font-size: 2.2rem;
      font-weight: 400;
      color: var(--text-main);
    }}

    .stat-value.orange-val {{
      color: var(--accent-orange);
    }}

    .stat-sub {{
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: 0.15rem;
      font-weight: 300;
    }}

    /* Control Panel */
    .control-panel {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      padding: 1.25rem 1.5rem;
      margin-bottom: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }}

    .top-actions-row {{
      display: flex;
      gap: 1rem;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      border-bottom: 1px solid #27272a;
      padding-bottom: 1rem;
    }}

    .download-info {{
      font-size: 0.95rem;
      color: var(--text-muted);
      font-weight: 300;
    }}

    .download-btns {{
      display: flex;
      gap: 0.75rem;
      align-items: center;
      transition: opacity 0.2s ease;
    }}

    .btn-download {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.6rem 1.2rem;
      border-radius: var(--radius-md);
      font-family: 'Work Sans', sans-serif;
      font-size: 0.88rem;
      font-weight: 400;
      cursor: pointer;
      transition: all 0.2s ease;
      text-decoration: none;
      border: 1px solid transparent;
    }}

    .btn-download-json {{
      background: #18181b;
      color: #ffffff;
      border-color: #3f3f46;
    }}

    .btn-download-json:hover {{
      background: #27272a;
      border-color: #a1a1aa;
    }}

    .btn-download-csv {{
      background: rgba(255, 140, 0, 0.15);
      color: var(--accent-orange);
      border-color: rgba(255, 140, 0, 0.4);
    }}

    .btn-download-csv:hover {{
      background: var(--accent-orange);
      color: #000000;
      font-weight: 500;
      box-shadow: 0 0 15px var(--accent-orange-glow);
    }}

    .search-row {{
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
    }}

    .search-box {{
      flex: 1;
      min-width: 280px;
      position: relative;
    }}

    .search-input {{
      width: 100%;
      padding: 0.85rem 1.25rem;
      padding-left: 2.8rem;
      background: #09090b;
      border: 1px solid var(--card-border);
      border-radius: var(--radius-md);
      color: var(--text-main);
      font-family: 'Work Sans', sans-serif;
      font-weight: 300;
      font-size: 0.95rem;
      outline: none;
      transition: border-color 0.2s ease;
    }}

    .search-input:focus {{
      border-color: var(--accent-orange);
    }}

    .search-icon {{
      position: absolute;
      left: 1rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      pointer-events: none;
    }}

    .filter-group-container {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      align-items: center;
      justify-content: space-between;
    }}

    .pills-group {{
      display: flex;
      gap: 0.5rem;
      align-items: center;
      flex-wrap: wrap;
    }}

    .group-label {{
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: 400;
      margin-right: 0.25rem;
    }}

    .pill {{
      padding: 0.45rem 0.9rem;
      background: #09090b;
      border: 1px solid var(--card-border);
      border-radius: 9999px;
      font-family: 'Work Sans', sans-serif;
      font-size: 0.85rem;
      font-weight: 300;
      color: var(--text-muted);
      cursor: pointer;
      user-select: none;
      transition: all 0.2s ease;
    }}

    .pill:hover {{
      color: var(--text-main);
      border-color: #52525b;
    }}

    .pill.active {{
      background: var(--accent-orange);
      color: #000000;
      font-weight: 500;
      border-color: var(--accent-orange);
    }}

    select.custom-select {{
      padding: 0.5rem 1rem;
      background: #09090b;
      border: 1px solid var(--card-border);
      border-radius: var(--radius-md);
      color: var(--text-main);
      font-family: 'Work Sans', sans-serif;
      font-weight: 300;
      font-size: 0.85rem;
      outline: none;
      cursor: pointer;
    }}

    select.custom-select:focus {{
      border-color: var(--accent-orange);
    }}

    /* Data Table Styling */
    .table-container {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      overflow-x: auto;
      position: relative;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.9rem;
    }}

    th {{
      background: #09090b;
      color: var(--accent-orange); /* Orange Heading Highlight */
      font-family: 'Work Sans', sans-serif;
      font-weight: 400; /* Work Sans Regular */
      padding: 1rem 0.9rem;
      border-bottom: 1px solid var(--card-border);
      cursor: pointer;
      user-select: none;
      white-space: nowrap;
      transition: color 0.2s ease;
    }}

    th:hover {{
      color: #ffffff;
    }}

    td {{
      padding: 0.85rem 0.9rem;
      border-bottom: 1px solid #1f1f23;
      color: #e4e4e7;
      white-space: nowrap;
      font-weight: 300; /* Work Sans Light */
    }}

    tbody tr {{
      transition: background-color 0.15s ease;
      cursor: pointer;
    }}

    tbody tr:hover {{
      background: #1f1f23;
    }}

    /* Sticky Details Column */
    th.sticky-col, td.sticky-col {{
      position: sticky;
      right: 0;
      background: #121215;
      z-index: 3;
      border-left: 1px solid #27272a;
      box-shadow: -4px 0 8px rgba(0, 0, 0, 0.5);
      text-align: center;
    }}

    tbody tr:hover td.sticky-col {{
      background: #27272a;
    }}

    /* Graphical Visualizer Panel */
    .graph-panel {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      margin-bottom: 1.5rem;
    }}

    .graph-controls {{
      display: flex;
      gap: 1.5rem;
      align-items: center;
      flex-wrap: wrap;
      margin-bottom: 1.25rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid #27272a;
    }}

    .axis-selector {{
      display: flex;
      gap: 0.5rem;
      align-items: center;
    }}

    .axis-label {{
      font-family: 'Work Sans', sans-serif;
      font-weight: 400;
      font-size: 0.9rem;
      color: var(--accent-orange);
    }}

    .chart-box {{
      position: relative;
      width: 100%;
      height: 540px;
      cursor: pointer;
    }}

    /* Badges */
    .badge {{
      display: inline-block;
      padding: 0.2rem 0.6rem;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 400;
    }}

    .badge-softwood {{
      background: #18181b;
      color: #ffffff;
      border: 1px solid #3f3f46;
    }}

    .badge-hardwood {{
      background: rgba(255, 140, 0, 0.15);
      color: var(--accent-orange);
      border: 1px solid rgba(255, 140, 0, 0.3);
    }}

    .badge-green {{
      background: #18181b;
      color: #a1a1aa;
      border: 1px solid #27272a;
    }}

    .badge-ad {{
      background: rgba(255, 140, 0, 0.1);
      color: #ffb86c;
      border: 1px solid rgba(255, 140, 0, 0.25);
    }}

    .badge-source-1983 {{
      background: #1e1e24;
      color: #a1a1aa;
      border: 1px solid #3f3f46;
    }}

    .badge-source-1997 {{
      background: rgba(59, 130, 246, 0.15);
      color: #60a5fa;
      border: 1px solid rgba(59, 130, 246, 0.3);
    }}

    .btn-detail {{
      padding: 0.4rem 0.85rem;
      background: rgba(255, 140, 0, 0.12);
      color: var(--accent-orange);
      border: 1px solid rgba(255, 140, 0, 0.35);
      border-radius: 6px;
      font-family: 'Work Sans', sans-serif;
      font-size: 0.8rem;
      font-weight: 400;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .btn-detail:hover {{
      background: var(--accent-orange);
      color: #000000;
      font-weight: 500;
    }}

    /* Modal / Drawer for Species Detail */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(4px);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 100;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease;
      padding: 1.5rem;
    }}

    .modal-backdrop.active {{
      opacity: 1;
      pointer-events: auto;
    }}

    .modal-card {{
      background: #141417;
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      max-width: 850px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 2rem;
      position: relative;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8);
      transform: scale(0.95);
      transition: transform 0.25s ease;
    }}

    .modal-backdrop.active .modal-card {{
      transform: scale(1);
    }}

    .close-btn {{
      position: absolute;
      top: 1.25rem;
      right: 1.25rem;
      background: #27272a;
      border: none;
      color: var(--text-muted);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 1.2rem;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.2s;
    }}

    .close-btn:hover {{
      background: var(--accent-orange);
      color: #000000;
    }}

    .modal-header {{
      margin-bottom: 1.5rem;
      padding-right: 2rem;
    }}

    .modal-title {{
      font-family: 'Work Sans', sans-serif;
      font-size: 1.8rem;
      font-weight: 400;
      color: var(--accent-orange); /* Orange Header */
    }}

    .modal-subtitle {{
      color: var(--text-muted);
      font-style: italic;
      font-size: 1.05rem;
      margin-bottom: 0.5rem;
    }}

    .properties-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 1rem;
      margin-top: 1.5rem;
    }}

    .prop-box {{
      background: #09090b;
      border: 1px solid #27272a;
      border-radius: var(--radius-md);
      padding: 1rem;
    }}

    .prop-name {{
      font-size: 0.8rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.35rem;
      font-weight: 300;
    }}

    .prop-val {{
      font-family: 'Work Sans', sans-serif;
      font-size: 1.3rem;
      font-weight: 400;
      color: var(--text-main);
    }}

    .prop-stats {{
      font-size: 0.75rem;
      color: #71717a;
      margin-top: 0.25rem;
    }}

    .empty-state {{
      text-align: center;
      padding: 3rem;
      color: var(--text-muted);
      font-size: 1.1rem;
      font-weight: 300;
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="badge-top">Building Research Establishment (BRE) Data Series</div>
      <h1>The Strength Properties of Timber</h1>
      <p class="subtitle">Interactive Dataset Explorer & Graphical Visualizer (447 Records across 1983 Master & 1997 Supplement)</p>
    </header>

    <!-- About / Data Sources Intro Card -->
    <div class="about-card">
      <div class="about-title">
        <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
        </svg>
        About This Dataset & Primary Sources
      </div>
      <div class="about-text">
        This database digitizes physical and mechanical timber properties evaluated by the UK <strong>Building Research Establishment (BRE) / Forest Products Research Laboratory (FPRL)</strong> using standardized small clear specimens ($20 \\times 20\\text{{ mm}}$ cross-section) in accordance with British Standard <strong>BS 373:1957</strong>.
      </div>
      
      <div class="sources-list">
        <div class="source-box">
          <div class="source-name">📘 1983 Master Report (Lavers / Moore)</div>
          <div class="source-desc">
            <a class="source-link" href="https://bregroup.com/store/bookshop/the-strength-properties-of-timber" target="_blank" rel="noopener">The Strength Properties of Timber</a> (BRE Report BR 241, 3rd Edition by Gwendoline M. Lavers, revised by G.L. Moore). Contains <strong>435 test records</strong> covering 223 timber species and growth location lots in both <em>Green (unseasoned)</em> and <em>Air-Dried (12% MC)</em> conditions.
          </div>
        </div>
        <div class="source-box">
          <div class="source-name">📙 1997 Supplement (Maun & Coday)</div>
          <div class="source-desc">
            <a class="source-link" href="https://bregroup.com/store/bookshop/the-strength-properties-of-timber-1997-supplement" target="_blank" rel="noopener">The Strength Properties of Timber: 1997 Supplement</a> (BRE Report BR 329 by K.W. Maun & A.E. Coday). Adds <strong>12 commercial & plantation-grown timber species</strong> (e.g. Andiroba, Bintangor, Kamarare, Taun, Vitex, Plantation Teak, Rubberwood) tested in air-dried condition.
          </div>
        </div>
      </div>
    </div>

    <!-- View Switcher Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" id="tab-btn-table" onclick="switchView('table')">
        <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M3 14h18M5 6h14a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2z"/>
        </svg>
        Tabular Data View
      </button>
      <button class="tab-btn" id="tab-btn-graph" onclick="switchView('graph')">
        <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a2 2 0 01-2 2H6a2 2 0 01-2-2V4z"/>
        </svg>
        Graphical Scatter Plot View
      </button>
    </div>

    <!-- Summary Metrics -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-label">Total Test Records</div>
        <div class="stat-value orange-val" id="stat-total-records">447</div>
        <div class="stat-sub">435 Records (1983 Lavers) + 12 Records (1997 Maun)</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Total Unique Species</div>
        <div class="stat-value" style="color: #ffffff;" id="stat-unique-species">191</div>
        <div class="stat-sub">186 Lavers Species + 5 New Maun Supplement Species</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Primary BRE Publications</div>
        <div class="stat-value orange-val">2 Reports</div>
        <div class="stat-sub">1983 Master (BR 241) & 1997 Supplement (BR 329)</div>
      </div>
    </div>

    <!-- Universal Control Panel -->
    <div class="control-panel">
      <!-- TOP Download Buttons Row (Table View Only) -->
      <div class="top-actions-row">
        <div class="download-info">
          Showing <strong id="visible-count" style="color: var(--accent-orange); font-weight: 400;">447</strong> test records (filtered view)
        </div>
        <div class="download-btns" id="download-btns-container">
          <button class="btn-download btn-download-json" onclick="downloadFilteredJSON()">
            <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
            </svg>
            Download Filtered JSON
          </button>
          <button class="btn-download btn-download-csv" onclick="downloadFilteredCSV()">
            <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3M3 17V7a2 2 0 012-2h6l2 2h7a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2z"/>
            </svg>
            Download Filtered CSV
          </button>
        </div>
      </div>

      <div class="search-row">
        <div class="search-box">
          <svg class="search-icon" width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
          </svg>
          <input type="text" id="search-input" class="search-input" placeholder="Search by Common Name, Botanical Name, Origin, or Source (e.g., Teak, Andiroba, 1997, Ghana)...">
        </div>
      </div>

      <div class="filter-group-container">
        <!-- Dataset Source Filter -->
        <div class="pills-group">
          <span class="group-label">Source:</span>
          <button class="pill active" data-filter-type="source" data-value="ALL">All Sources</button>
          <button class="pill" data-filter-type="source" data-value="1983">1983 Report (Lavers)</button>
          <button class="pill" data-filter-type="source" data-value="1997">1997 Supplement (Maun)</button>
        </div>

        <!-- Class Filter -->
        <div class="pills-group">
          <span class="group-label">Class:</span>
          <button class="pill active" data-filter-type="class" data-value="ALL">All</button>
          <button class="pill" data-filter-type="class" data-value="Softwoods">Softwoods</button>
          <button class="pill" data-filter-type="class" data-value="Hardwoods">Hardwoods</button>
        </div>

        <!-- Condition Filter -->
        <div class="pills-group">
          <span class="group-label">Condition:</span>
          <button class="pill active" data-filter-type="condition" data-value="ALL">All</button>
          <button class="pill" data-filter-type="condition" data-value="G.">Green (G.)</button>
          <button class="pill" data-filter-type="condition" data-value="A.D.">Air-dried (A.D.)</button>
        </div>

        <!-- Origin Select & Sort -->
        <div style="display: flex; gap: 0.75rem; align-items: center;">
          <select id="origin-select" class="custom-select">
            <option value="ALL">All Origins</option>
          </select>

          <select id="sort-select" class="custom-select">
            <option value="id-asc">Sort: ID (Default)</option>
            <option value="name-asc">Name (A-Z)</option>
            <option value="mor-desc">MOR Bending (High to Low)</option>
            <option value="moe-desc">MOE Stiffness (High to Low)</option>
            <option value="density-desc">Density (High to Low)</option>
            <option value="hardness-desc">Hardness (High to Low)</option>
          </select>
        </div>
      </div>
    </div>

    <!-- VIEW 1: Data Table View -->
    <div id="view-table" class="table-container">
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Source</th>
            <th>Species Common Name</th>
            <th>Botanical Name</th>
            <th>Origin</th>
            <th>Class</th>
            <th>Cond</th>
            <th>Density (kg/m³)</th>
            <th>SG</th>
            <th>MOR (MPa)</th>
            <th>MOE (MPa)</th>
            <th>Compression (MPa)</th>
            <th>Hardness (N)</th>
            <th class="sticky-col">Details</th>
          </tr>
        </thead>
        <tbody id="table-body">
          <!-- Populated by JS -->
        </tbody>
      </table>
      <div id="empty-msg" class="empty-state" style="display: none;">
        No matching timber species found. Try clearing your filters or search term.
      </div>
    </div>

    <!-- VIEW 2: Graphical Scatter Plot Visualizer View -->
    <div id="view-graph" class="graph-panel" style="display: none;">
      <div class="graph-controls">
        <div class="axis-selector">
          <span class="axis-label">X-Axis Property:</span>
          <select id="x-axis-select" class="custom-select" onchange="updateChart()">
            <option value="density">Density (kg/m³)</option>
            <option value="sg">Specific Gravity</option>
            <option value="mor" selected>Bending MOR (MPa)</option>
            <option value="moe">Bending MOE (MPa)</option>
            <option value="comp">Compression Parallel (MPa)</option>
            <option value="hardness">Side Hardness (N)</option>
            <option value="shear">Shear Parallel (MPa)</option>
            <option value="work_max">Work to Max Load (mm N/mm³)</option>
            <option value="impact">Impact Drop Height (m)</option>
          </select>
        </div>

        <div class="axis-selector">
          <span class="axis-label">Y-Axis Property:</span>
          <select id="y-axis-select" class="custom-select" onchange="updateChart()">
            <option value="density">Density (kg/m³)</option>
            <option value="sg">Specific Gravity</option>
            <option value="mor">Bending MOR (MPa)</option>
            <option value="moe" selected>Bending MOE (MPa)</option>
            <option value="comp">Compression Parallel (MPa)</option>
            <option value="hardness">Side Hardness (N)</option>
            <option value="shear">Shear Parallel (MPa)</option>
            <option value="work_max">Work to Max Load (mm N/mm³)</option>
            <option value="impact">Impact Drop Height (m)</option>
          </select>
        </div>

        <div style="margin-left: auto; color: var(--accent-orange); font-size: 0.88rem; font-weight: 300;">
          💡 Click on any scatter point to view full species details modal
        </div>
      </div>

      <div class="chart-box">
        <canvas id="scatterChart"></canvas>
      </div>
    </div>
  </div>

  <!-- Detail Modal -->
  <div class="modal-backdrop" id="modal">
    <div class="modal-card">
      <button class="close-btn" id="modal-close">&times;</button>
      <div class="modal-header">
        <h2 class="modal-title" id="m-title">Species Name</h2>
        <div class="modal-subtitle" id="m-botanical">Botanical Name</div>
        <div style="display: flex; gap: 0.5rem; margin-top: 0.5rem; flex-wrap: wrap;" id="m-badges"></div>
      </div>

      <div class="properties-grid" id="m-grid">
        <!-- Populated by JS -->
      </div>
    </div>
  </div>

  <script>
    const DATA = {json_data_str};

    let activeView = 'table'; // 'table' or 'graph'
    let activeSource = 'ALL';
    let activeClass = 'ALL';
    let activeCondition = 'ALL';
    let activeOrigin = 'ALL';
    let currentSort = 'id-asc';
    let searchTerm = '';
    let currentFiltered = [...DATA];
    let scatterChart = null;

    // Elements
    const tableBody = document.getElementById('table-body');
    const searchInput = document.getElementById('search-input');
    const originSelect = document.getElementById('origin-select');
    const sortSelect = document.getElementById('sort-select');
    const emptyMsg = document.getElementById('empty-msg');
    const visibleCount = document.getElementById('visible-count');
    const downloadBtnsContainer = document.getElementById('download-btns-container');

    const modal = document.getElementById('modal');
    const modalClose = document.getElementById('modal-close');

    // Populate Origins
    const origins = Array.from(new Set(DATA.map(d => d.origin).filter(Boolean))).sort();
    origins.forEach(o => {{
      const opt = document.createElement('option');
      opt.value = o;
      opt.textContent = o;
      originSelect.appendChild(opt);
    }});

    // Tab Switcher
    window.switchView = function(view) {{
      activeView = view;
      document.getElementById('tab-btn-table').classList.toggle('active', view === 'table');
      document.getElementById('tab-btn-graph').classList.toggle('active', view === 'graph');

      document.getElementById('view-table').style.display = view === 'table' ? 'block' : 'none';
      document.getElementById('view-graph').style.display = view === 'graph' ? 'block' : 'none';

      // Hide download buttons on Graphical Plot view
      downloadBtnsContainer.style.display = view === 'table' ? 'flex' : 'none';

      if (view === 'graph') updateChart();
    }};

    // Event Listeners for Filters
    document.querySelectorAll('.pill').forEach(btn => {{
      btn.addEventListener('click', (e) => {{
        const group = btn.dataset.filterType;
        const val = btn.dataset.value;

        // Toggle active within group
        document.querySelectorAll(`.pill[data-filter-type="${{group}}"]`).forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        if (group === 'source') activeSource = val;
        if (group === 'class') activeClass = val;
        if (group === 'condition') activeCondition = val;

        render();
      }});
    }});

    searchInput.addEventListener('input', (e) => {{
      searchTerm = e.target.value.toLowerCase().trim();
      render();
    }});

    originSelect.addEventListener('change', (e) => {{
      activeOrigin = e.target.value;
      render();
    }});

    sortSelect.addEventListener('change', (e) => {{
      currentSort = e.target.value;
      render();
    }});

    modalClose.addEventListener('click', () => modal.classList.remove('active'));
    modal.addEventListener('click', (e) => {{
      if (e.target === modal) modal.classList.remove('active');
    }});

    function getTripleVal(triple, key='mean') {{
      if (triple && triple[key] !== null && triple[key] !== undefined) return triple[key];
      return null;
    }}

    function getPropertyValue(d, propKey) {{
      if (propKey === 'density') return d.condition === 'G.' ? d.density_50mc_kg_m3 : d.density_12mc_kg_m3;
      if (propKey === 'sg') return getTripleVal(d.specific_gravity);
      if (propKey === 'mor') return getTripleVal(d.static_bending_mor_mpa);
      if (propKey === 'moe') return getTripleVal(d.static_bending_moe_mpa);
      if (propKey === 'comp') return getTripleVal(d.compression_parallel_mpa);
      if (propKey === 'hardness') return getTripleVal(d.hardness_side_grain_n);
      if (propKey === 'shear') return getTripleVal(d.shear_parallel_mpa);
      if (propKey === 'work_max') return getTripleVal(d.work_to_maximum_load_mm_N_mm3);
      if (propKey === 'impact') return getTripleVal(d.impact_drop_height_m);
      return null;
    }}

    function getPropLabel(key) {{
      const labels = {{
        density: 'Density (kg/m³)',
        sg: 'Specific Gravity',
        mor: 'Bending MOR (MPa)',
        moe: 'Bending MOE (MPa)',
        comp: 'Compression Parallel (MPa)',
        hardness: 'Side Hardness (N)',
        shear: 'Shear Parallel (MPa)',
        work_max: 'Work to Max Load (mm N/mm³)',
        impact: 'Impact Drop Height (m)'
      }};
      return labels[key] || key;
    }}

    function render() {{
      currentFiltered = DATA.filter(d => {{
        if (activeSource === '1983' && !d.dataset_source.includes('1983')) return false;
        if (activeSource === '1997' && !d.dataset_source.includes('1997')) return false;

        if (activeClass !== 'ALL' && !d.class.includes(activeClass)) return false;
        if (activeCondition !== 'ALL' && d.condition !== activeCondition) return false;
        if (activeOrigin !== 'ALL' && d.origin !== activeOrigin) return false;

        if (searchTerm) {{
          const matchCommon = (d.species_common_name || '').toLowerCase().includes(searchTerm);
          const matchBotanical = (d.species_botanical_name || '').toLowerCase().includes(searchTerm);
          const matchOrigin = (d.origin || '').toLowerCase().includes(searchTerm);
          const matchSource = (d.dataset_source || '').toLowerCase().includes(searchTerm);
          if (!matchCommon && !matchBotanical && !matchOrigin && !matchSource) return false;
        }}
        return true;
      }});

      // Sorting
      currentFiltered.sort((a, b) => {{
        if (currentSort === 'name-asc') return (a.species_common_name || '').localeCompare(b.species_common_name || '');
        if (currentSort === 'mor-desc') return (getTripleVal(b.static_bending_mor_mpa) || 0) - (getTripleVal(a.static_bending_mor_mpa) || 0);
        if (currentSort === 'moe-desc') return (getTripleVal(b.static_bending_moe_mpa) || 0) - (getTripleVal(a.static_bending_moe_mpa) || 0);
        if (currentSort === 'density-desc') {{
          const densA = a.density_50mc_kg_m3 || a.density_12mc_kg_m3 || 0;
          const densB = b.density_50mc_kg_m3 || b.density_12mc_kg_m3 || 0;
          return densB - densA;
        }}
        if (currentSort === 'hardness-desc') return (getTripleVal(b.hardness_side_grain_n) || 0) - (getTripleVal(a.hardness_side_grain_n) || 0);
        
        // Default sort: Numeric ID if integer, otherwise String ID
        const idA = typeof a.id === 'number' ? a.id : 999;
        const idB = typeof b.id === 'number' ? b.id : 999;
        if (idA !== idB) return idA - idB;
        return (a.id + '').localeCompare(b.id + '');
      }});

      visibleCount.textContent = currentFiltered.length;

      // Render Table Rows
      tableBody.innerHTML = '';
      if (currentFiltered.length === 0) {{
        emptyMsg.style.display = 'block';
      }} else {{
        emptyMsg.style.display = 'none';
        currentFiltered.forEach(d => {{
          const tr = document.createElement('tr');
          
          const density = d.condition === 'G.' ? (d.density_50mc_kg_m3 || '-') : (d.density_12mc_kg_m3 || '-');
          const sg = getTripleVal(d.specific_gravity);
          const mor = getTripleVal(d.static_bending_mor_mpa);
          const moe = getTripleVal(d.static_bending_moe_mpa);
          const comp = getTripleVal(d.compression_parallel_mpa);
          const hardness = getTripleVal(d.hardness_side_grain_n);

          const is1997 = d.dataset_source.includes('1997');
          const sourceBadge = is1997 ? '<span class="badge badge-source-1997">1997 Supp.</span>' : '<span class="badge badge-source-1983">1983 Report</span>';

          const isSoftwood = d.class.includes('Softwood');
          const classBadge = isSoftwood ? '<span class="badge badge-softwood">Softwood</span>' : '<span class="badge badge-hardwood">Hardwood</span>';
          const condBadge = d.condition === 'G.' ? '<span class="badge badge-green">G. Green</span>' : '<span class="badge badge-ad">A.D. Air-dried</span>';

          tr.innerHTML = `
            <td style="color: var(--text-muted); font-size: 0.8rem;">#${{d.id}}</td>
            <td>${{sourceBadge}}</td>
            <td style="font-weight: 400; color: #ffffff;">${{d.species_common_name || '-'}}</td>
            <td style="font-style: italic; color: #a1a1aa;">${{d.species_botanical_name || '-'}}</td>
            <td>${{d.origin || '-'}}</td>
            <td>${{classBadge}}</td>
            <td>${{condBadge}}</td>
            <td style="font-weight: 400;">${{density}}</td>
            <td>${{sg !== null ? sg : '-'}}</td>
            <td style="color: var(--accent-orange); font-weight: 500;">${{mor !== null ? mor : '-'}}</td>
            <td style="color: #ffffff; font-weight: 400;">${{moe !== null ? moe : '-'}}</td>
            <td>${{comp !== null ? comp : '-'}}</td>
            <td>${{hardness !== null ? hardness : '-'}}</td>
            <td class="sticky-col"><button class="btn-detail" onclick="openDetail('${{d.id}}')">View</button></td>
          `;

          tr.addEventListener('click', (e) => {{
            if (!e.target.classList.contains('btn-detail')) openDetail(d.id);
          }});

          tableBody.appendChild(tr);
        }});
      }}

      if (activeView === 'graph') updateChart();
    }}

    // Update Graphical Scatter Plot
    function updateChart() {{
      const xProp = document.getElementById('x-axis-select').value;
      const yProp = document.getElementById('y-axis-select').value;

      const softwoodsPoints = [];
      const hardwoodsPoints = [];

      currentFiltered.forEach(d => {{
        const xVal = getPropertyValue(d, xProp);
        const yVal = getPropertyValue(d, yProp);

        if (xVal !== null && yVal !== null && typeof xVal === 'number' && typeof yVal === 'number') {{
          const pt = {{
            x: xVal,
            y: yVal,
            item: d
          }};
          if (d.class.includes('Softwood')) {{
            softwoodsPoints.push(pt);
          }} else {{
            hardwoodsPoints.push(pt);
          }}
        }}
      }});

      const ctx = document.getElementById('scatterChart').getContext('2d');

      if (scatterChart) scatterChart.destroy();

      scatterChart = new Chart(ctx, {{
        type: 'scatter',
        data: {{
          datasets: [
            {{
              label: 'Softwoods',
              data: softwoodsPoints,
              backgroundColor: 'rgba(255, 255, 255, 0.85)', // White for Softwoods
              borderColor: '#ffffff',
              pointRadius: 6,
              pointHoverRadius: 10,
              pointHoverBackgroundColor: 'rgb(255, 140, 0)'
            }},
            {{
              label: 'Hardwoods',
              data: hardwoodsPoints,
              backgroundColor: 'rgba(255, 140, 0, 0.85)', // Orange (255, 140, 0) for Hardwoods
              borderColor: 'rgb(255, 140, 0)',
              pointRadius: 6,
              pointHoverRadius: 10,
              pointHoverBackgroundColor: '#ffffff'
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          onClick: function(event, elements) {{
            if (elements && elements.length > 0) {{
              const el = elements[0];
              const datasetIndex = el.datasetIndex;
              const index = el.index;
              const raw = scatterChart.data.datasets[datasetIndex].data[index];
              if (raw && raw.item && raw.item.id) {{
                openDetail(raw.item.id);
              }}
            }}
          }},
          plugins: {{
            legend: {{
              labels: {{
                color: '#f4f4f5',
                font: {{ family: 'Work Sans', size: 14, weight: '400' }}
              }}
            }},
            tooltip: {{
              backgroundColor: '#18181b',
              titleColor: 'rgb(255, 140, 0)',
              bodyColor: '#f4f4f5',
              borderColor: '#27272a',
              borderWidth: 1,
              padding: 12,
              displayColors: true,
              callbacks: {{
                title: function(context) {{
                  const item = context[0].raw.item;
                  return item.species_common_name + ' (' + item.condition + ')';
                }},
                label: function(context) {{
                  const item = context.raw.item;
                  return [
                    'Source: ' + item.dataset_source,
                    'Botanical: ' + (item.species_botanical_name || 'N/A'),
                    'Origin: ' + (item.origin || 'N/A'),
                    getPropLabel(xProp) + ': ' + context.raw.x,
                    getPropLabel(yProp) + ': ' + context.raw.y,
                    '(Click point to open details modal)'
                  ];
                }}
              }}
            }}
          }},
          scales: {{
            x: {{
              title: {{
                display: true,
                text: getPropLabel(xProp),
                color: 'rgb(255, 140, 0)', /* Orange (255, 140, 0) Axis Heading */
                font: {{ family: 'Work Sans', size: 14, weight: '400' }}
              }},
              grid: {{ color: 'rgba(255, 255, 255, 0.05)' }},
              ticks: {{ color: '#a1a1aa', font: {{ family: 'Work Sans', weight: '300' }} }}
            }},
            y: {{
              title: {{
                display: true,
                text: getPropLabel(yProp),
                color: 'rgb(255, 140, 0)', /* Orange (255, 140, 0) Axis Heading */
                font: {{ family: 'Work Sans', size: 14, weight: '400' }}
              }},
              grid: {{ color: 'rgba(255, 255, 255, 0.05)' }},
              ticks: {{ color: '#a1a1aa', font: {{ family: 'Work Sans', weight: '300' }} }}
            }}
          }}
        }}
      }});
    }}

    window.openDetail = function(id) {{
      const item = DATA.find(d => (d.id + '') === (id + ''));
      if (!item) return;

      document.getElementById('m-title').textContent = item.species_common_name || 'Unknown Species';
      document.getElementById('m-botanical').textContent = item.species_botanical_name || '';

      const is1997 = item.dataset_source.includes('1997');
      const sourceBadge = is1997 ? '<span class="badge badge-source-1997">Source: 1997 BRE Supplement (Maun & Coday)</span>' : '<span class="badge badge-source-1983">Source: 1983 BRE Report (Lavers)</span>';

      const badges = document.getElementById('m-badges');
      badges.innerHTML = `
        ${{sourceBadge}}
        <span class="badge ${{item.class.includes('Softwood') ? 'badge-softwood' : 'badge-hardwood'}}">${{item.class}}</span>
        <span class="badge ${{item.condition === 'G.' ? 'badge-green' : 'badge-ad'}}">${{item.condition === 'G.' ? 'Green (G.)' : 'Air-dried (A.D.)'}}</span>
        <span class="badge" style="background: #27272a; color: var(--text-main);">${{item.origin || 'Unknown Origin'}}</span>
      `;

      const grid = document.getElementById('m-grid');
      grid.innerHTML = '';

      const props = [
        {{ label: 'Dataset Source', val: item.dataset_source }},
        {{ label: 'Trees/Sticks Sampled', val: item.trees_sampled || '-' }},
        {{ label: 'Moisture Content (%)', val: item.moisture_content_pct !== null ? item.moisture_content_pct + '%' : '-' }},
        {{ label: 'Density (Green 50% MC)', val: item.density_50mc_kg_m3 ? item.density_50mc_kg_m3 + ' kg/m³' : '-' }},
        {{ label: 'Density (Air-Dried 12% MC)', val: item.density_12mc_kg_m3 ? item.density_12mc_kg_m3 + ' kg/m³' : '-' }},

        {{ label: 'Specific Gravity', triple: item.specific_gravity, unit: '' }},
        {{ label: 'Bending Strength MOR', triple: item.static_bending_mor_mpa, unit: 'MPa' }},
        {{ label: 'Bending Stiffness MOE', triple: item.static_bending_moe_mpa, unit: 'MPa' }},
        {{ label: 'Work to Max Load', triple: item.work_to_maximum_load_mm_N_mm3, unit: 'mm N/mm³' }},
        {{ label: 'Work Total Fracture', triple: item.work_total_fracture_mm_N_mm3, unit: 'mm N/mm³' }},
        {{ label: 'Impact Drop Height', triple: item.impact_drop_height_m, unit: 'm' }},
        {{ label: 'Compression Parallel', triple: item.compression_parallel_mpa, unit: 'MPa' }},
        {{ label: 'Hardness (Side Grain)', triple: item.hardness_side_grain_n, unit: 'N' }},
        {{ label: 'Shear Parallel', triple: item.shear_parallel_mpa, unit: 'MPa' }},
        {{ label: 'Cleavage (Radial)', triple: item.cleavage_radial_n_mm, unit: 'N/mm' }},
        {{ label: 'Cleavage (Tangential)', triple: item.cleavage_tangential_n_mm, unit: 'N/mm' }},
      ];

      if (item.notes) {{
        props.unshift({{ label: 'Testing / Supply Notes', val: item.notes }});
      }}

      props.forEach(p => {{
        const box = document.createElement('div');
        box.className = 'prop-box';

        if (p.triple) {{
          const mean = p.triple.mean !== null && p.triple.mean !== undefined ? p.triple.mean : '-';
          const std = p.triple.std !== null && p.triple.std !== undefined ? p.triple.std : 'N/A';
          const n = p.triple.n !== null && p.triple.n !== undefined ? p.triple.n : 'N/A';
          box.innerHTML = `
            <div class="prop-name">${{p.label}}</div>
            <div class="prop-val">${{mean}} <span style="font-size: 0.8rem; font-weight: 300; color: var(--text-muted);">${{p.unit}}</span></div>
            <div class="prop-stats">std: ${{std}} • n: ${{n}}</div>
          `;
        }} else {{
          box.innerHTML = `
            <div class="prop-name">${{p.label}}</div>
            <div class="prop-val">${{p.val || '-'}}</div>
          `;
        }}
        grid.appendChild(box);
      }});

      modal.classList.add('active');
    }};

    // Download Filtered Results as JSON
    window.downloadFilteredJSON = function() {{
      const jsonStr = JSON.stringify(currentFiltered, null, 2);
      const blob = new Blob([jsonStr], {{ type: 'application/json' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `combined_timber_filtered_${{currentFiltered.length}}_records.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }};

    // Download Filtered Results as CSV
    window.downloadFilteredCSV = function() {{
      if (currentFiltered.length === 0) return;

      const headers = [
        "id", "dataset_source", "class", "species_common_name", "species_botanical_name", "origin", "condition",
        "trees_sampled", "moisture_content_pct", "density_50mc_kg_m3", "density_12mc_kg_m3",
        "specific_gravity_mean", "specific_gravity_std", "specific_gravity_n",
        "static_bending_mor_mpa_mean", "static_bending_mor_mpa_std", "static_bending_mor_mpa_n",
        "static_bending_moe_mpa_mean", "static_bending_moe_mpa_std", "static_bending_moe_mpa_n",
        "work_to_maximum_load_mean", "work_to_maximum_load_std", "work_to_maximum_load_n",
        "work_total_fracture_mean", "work_total_fracture_std", "work_total_fracture_n",
        "impact_drop_height_m_mean", "impact_drop_height_m_std", "impact_drop_height_m_n",
        "compression_parallel_mpa_mean", "compression_parallel_mpa_std", "compression_parallel_mpa_n",
        "hardness_side_grain_n_mean", "hardness_side_grain_n_std", "hardness_side_grain_n_n",
        "shear_parallel_mpa_mean", "shear_parallel_mpa_std", "shear_parallel_mpa_n",
        "cleavage_radial_n_mm_mean", "cleavage_radial_n_mm_std", "cleavage_radial_n_mm_n",
        "cleavage_tangential_n_mm_mean", "cleavage_tangential_n_mm_std", "cleavage_tangential_n_mm_n"
      ];

      const csvRows = [headers.join(",")];

      currentFiltered.forEach(r => {{
        const row = [
          `"${{r.id}}"`,
          `"${{(r.dataset_source || '').replace(/"/g, '""')}}"`,
          `"${{(r.class || '').replace(/"/g, '""')}}"`,
          `"${{(r.species_common_name || '').replace(/"/g, '""')}}"`,
          `"${{(r.species_botanical_name || '').replace(/"/g, '""')}}"`,
          `"${{(r.origin || '').replace(/"/g, '""')}}"`,
          `"${{(r.condition || '').replace(/"/g, '""')}}"`,
          `"${{(r.trees_sampled || '').replace(/"/g, '""')}}"`,
          r.moisture_content_pct !== null ? r.moisture_content_pct : "",
          r.density_50mc_kg_m3 !== null && r.density_50mc_kg_m3 !== undefined ? r.density_50mc_kg_m3 : "",
          r.density_12mc_kg_m3 !== null && r.density_12mc_kg_m3 !== undefined ? r.density_12mc_kg_m3 : "",

          getTripleVal(r.specific_gravity, 'mean') ?? "",
          getTripleVal(r.specific_gravity, 'std') ?? "",
          getTripleVal(r.specific_gravity, 'n') ?? "",

          getTripleVal(r.static_bending_mor_mpa, 'mean') ?? "",
          getTripleVal(r.static_bending_mor_mpa, 'std') ?? "",
          getTripleVal(r.static_bending_mor_mpa, 'n') ?? "",

          getTripleVal(r.static_bending_moe_mpa, 'mean') ?? "",
          getTripleVal(r.static_bending_moe_mpa, 'std') ?? "",
          getTripleVal(r.static_bending_moe_mpa, 'n') ?? "",

          getTripleVal(r.work_to_maximum_load_mm_N_mm3, 'mean') ?? "",
          getTripleVal(r.work_to_maximum_load_mm_N_mm3, 'std') ?? "",
          getTripleVal(r.work_to_maximum_load_mm_N_mm3, 'n') ?? "",

          getTripleVal(r.work_total_fracture_mm_N_mm3, 'mean') ?? "",
          getTripleVal(r.work_total_fracture_mm_N_mm3, 'std') ?? "",
          getTripleVal(r.work_total_fracture_mm_N_mm3, 'n') ?? "",

          getTripleVal(r.impact_drop_height_m, 'mean') ?? "",
          getTripleVal(r.impact_drop_height_m, 'std') ?? "",
          getTripleVal(r.impact_drop_height_m, 'n') ?? "",

          getTripleVal(r.compression_parallel_mpa, 'mean') ?? "",
          getTripleVal(r.compression_parallel_mpa, 'std') ?? "",
          getTripleVal(r.compression_parallel_mpa, 'n') ?? "",

          getTripleVal(r.hardness_side_grain_n_mean, 'mean') ?? "",
          getTripleVal(r.hardness_side_grain_n, 'std') ?? "",
          getTripleVal(r.hardness_side_grain_n, 'n') ?? "",

          getTripleVal(r.shear_parallel_mpa, 'mean') ?? "",
          getTripleVal(r.shear_parallel_mpa, 'std') ?? "",
          getTripleVal(r.shear_parallel_mpa, 'n') ?? "",

          getTripleVal(r.cleavage_radial_n_mm, 'mean') ?? "",
          getTripleVal(r.cleavage_radial_n_mm, 'std') ?? "",
          getTripleVal(r.cleavage_radial_n_mm, 'n') ?? "",

          getTripleVal(r.cleavage_tangential_n_mm, 'mean') ?? "",
          getTripleVal(r.cleavage_tangential_n_mm, 'std') ?? "",
          getTripleVal(r.cleavage_tangential_n_mm, 'n') ?? ""
        ];
        csvRows.push(row.join(","));
      }});

      const csvStr = csvRows.join("\\n");
      const blob = new Blob([csvStr], {{ type: 'text/csv;charset=utf-8;' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `combined_timber_filtered_${{currentFiltered.length}}_records.csv`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }};

    // Initial Render
    render();
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Updated index.html created successfully with BRE store links!")
