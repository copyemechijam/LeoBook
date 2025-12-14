"""
LeoBook v2.6.0: Advanced Football Prediction & Betting System
A comprehensive AI-powered system that observes, analyzes, predicts, and executes betting strategies.

OVERVIEW:
LeoBook is an intelligent football prediction system that combines advanced data analysis, machine learning,
and automated betting execution. The system maintains persistent browser sessions for seamless login retention
across Flashscore.com and Football.com platforms.

CORE ARCHITECTURE:
- Dual-browser system (Flashscore + Football.com) with persistent login sessions
- Advanced prediction engine with 11+ betting markets support
- Self-learning AI with rule-based and ML components
- Automated outcome review with retry mechanisms
- Production-grade monitoring and health checks
- Comprehensive error handling and logging

MAIN WORKFLOW:
1. DATA COLLECTION PHASE:
   - Navigate to Flashscore.com/football scheduled matches
   - Extract match metadata (ID, URLs, teams, times) for upcoming fixtures
   - Sort matches chronologically and process earliest first
   - Visit match pages to extract H2H data, standings, and team statistics
   - Store comprehensive match data in structured CSV format

2. ANALYSIS & PREDICTION PHASE:
   - Process extracted data through RuleEngine (Neo/model.py)
   - Generate predictions across 11+ betting markets
   - Apply machine learning confidence scoring
   - Save predictions with detailed reasoning and confidence levels

3. BETTING EXECUTION PHASE:
   - Match predictions with Football.com betting markets
   - Use AI to identify safest betting opportunities
   - Execute automated bet placement with stake management
   - Track booking codes and bet statuses

4. OUTCOME REVIEW & LEARNING PHASE:
   - Monitor completed matches for results
   - Evaluate prediction accuracy across all markets
   - Update learning weights based on performance
   - Retrain ML models with new outcome data
   - Implement progressive retry logic for failed reviews

ADVANCED FEATURES:
- Health monitoring with automated alerts
- Production readiness validation
- Error rate tracking and threshold alerts
- Atomic CSV operations for data integrity
- Concurrent processing with semaphore controls
- Comprehensive logging and debugging capabilities

SUPPORTED BETTING MARKETS:
1. 1X2 (Home/Away/Draw)
2. Double Chance (Home or Draw, Away or Draw, Home or Away)
3. Draw No Bet (Home/Away excluding draw)
4. Both Teams To Score (Yes/No)
5. Over/Under Goals (0.5, 1.5, 2.5, 3.5, 4.5, 5.5)
6. Goal Ranges (0-1, 2-3, 4-6 goals)
7. Correct Score (exact score predictions)
8. Clean Sheet (team doesn't concede)
9. Asian Handicap (-1, +0.5, +1, etc.)
10. Combo Bets (Win & Over, Win & BTTS)
11. Team Over/Under (individual team goals)

SYSTEM COMPONENTS:

1. Leo.py (Main Controller)
   - Orchestrates entire prediction and betting workflow
   - Manages browser sessions and concurrent operations
   - Handles system initialization and cleanup

2. Sites/ (Data Sources)
   - flashscore.py: Match data extraction and H2H analysis
   - football_com.py: Betting market analysis and execution

3. Neo/ (AI Engine)
   - intelligence.py: Computer vision and selector management
   - model.py: Advanced prediction engine with learning capabilities

4. Helpers/ (Utility Systems)
   - DB_Helpers/: Database operations and outcome review
   - Neo_Helpers/: AI component management
   - Site_Helpers/: Web interaction utilities

5. DB/ (Data Storage)
   - predictions.csv: Core prediction data with outcomes
   - schedules.csv: Match scheduling and metadata
   - standings.csv: League standings and statistics
   - teams.csv: Team information and IDs
   - region_league.csv: League organization data
   - learning_weights.json: AI learning parameters
   - models/: Trained ML models (RF, GB)
   - auth/: Authentication state management

6. Logs/ (Monitoring & Debugging)
   - Error/: Failed operation artifacts and analysis
   - Page/: Page captures for debugging
   - Terminal/: Session logs and system events
   - review_errors.log: Prediction evaluation errors
   - health_status.json: System health metrics

PRODUCTION FEATURES:
- Health monitoring with configurable thresholds
- Automatic retry mechanisms (5s, 10s, 15s delays)
- Error rate alerting and performance tracking
- Production readiness validation
- Version compatibility checking
- Graceful degradation on failures

MAINTENANCE & MONITORING:
- Automated testing pipelines
- Health check intervals (5-minute cycles)
- Error threshold monitoring (10 errors = alert)
- Performance metrics collection
- Structured logging with severity levels

The system continuously learns and improves through outcome analysis,
adapting prediction weights and ML models based on real-world performance.
Failed predictions are automatically retried, ensuring comprehensive coverage
of all betting opportunities with minimal manual intervention.
"""
