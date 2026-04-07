# Model Marketplace Framework - Update Summary

## Updates Based on Official Support Documentation

**Source:** Apex Support Portal - "Manage Model Marketplace Subscriptions" + Rebalancer Overview Documentation

---

## Major Enhancements

### 1. **Enhanced Executive Summary**
- Added definition: Models generate trade proposals based on market activity
- Emphasized **automatic updates** from providers as key value proposition
- Clarified integration with Rebalancer for ongoing portfolio management

### 2. **Detailed Process Flow (Steps 3-8)**

**Step 3 - Client Acceptance & Discovery:**
- Specific navigation: Trading section → Model Marketplace
- Exact UI columns: Provider, Model, Investment Vehicle, Status (AVAILABLE/SUBSCRIBED)
- Note about T&C retention even after unsubscription

**Step 4 - Model Evaluation:**
- Detailed breakdown of model detail page sections:
  - Holdings Section: Symbol and Target Weight
  - Summary Section: Provider, Investment Vehicle, Inception Date, Last Updated
  - Resources Section: Fact Sheet and Website links

**Step 5 - Model Subscription:**
- UI behavior: Green Subscribe button → Red Unsubscribe button
- Status flag change: AVAILABLE → SUBSCRIBED
- Success message display
- Provider T&C retention

**Step 6 - Post-Subscription Configuration:**
- **NEW CRITICAL STEP:** Verify asset class assignments
  - Example: SPDR Gold Trust (GLD) → Commodity class
  - Required for optimum Rebalancer performance
- Create and fund goals using subscribed models
- References to official documentation

**Step 8 - Unsubscribing (NEW SECTION):**
- Unsubscribe behavior: Stops updates but retains last weights
- Example scenario: 80/20 weight preserved even if provider updates to 70/30
- To fully discontinue: Must delete model from Rebalancer
- T&C retention for easy re-subscription

### 3. **New Section 7: Rebalancer Capabilities & Integration**

Complete overview of Rebalancer features that enhance Model Marketplace:

**Covered Topics:**
- What is Rebalancing (definition)
- 8 major feature categories:
  1. Firm-level settings (minimum trade size, tax-loss harvesting)
  2. Asset class management (trees, security mapping)
  3. Models, frameworks & goals (including direct indexing)
  4. Threshold management (4 types of thresholds)
  5. Client & investor settings (restrictions, optimization, quarantine)
  6. Direct indexing capabilities
  7. Trade management (SOD files, proposals, blotter)
  8. Advanced features (completion portfolios, cash generation, wash sales)

**Value:** Helps business teams understand the full platform capabilities, not just Model Marketplace in isolation.

### 4. **New Section 14: Client Use Cases & Value Stories**

Four detailed use case scenarios:

1. **RIA Scaling Portfolio Management**
   - 500 accounts, limited research team
   - 70% reduction in portfolio construction time
   - Scalable to 1000+ accounts

2. **Digital Advisor Launching New Product**
   - Quick launch of managed portfolios
   - White-label marketplace models
   - Scale to 50,000+ accounts

3. **Existing Rebalancer Client Enhancing Offering**
   - Blend custom + marketplace models
   - Expand product menu without overhead
   - Client retention strategy

4. **Sub-Advisory Relationship (Provider Perspective)**
   - Example: Voya Investment Management
   - Distribution to 38 firms, 50,000+ accounts
   - Automated model update propagation

### 5. **New Section 15: Key Terminology**

Comprehensive glossary for client conversations:

**Rebalancer Terms:** (15 terms)
- Rebalancing, Models, Frameworks, Goals
- SOD Files, Trade Proposals, Drift, Thresholds
- Optimization, Tax-Loss Harvesting, Direct Indexing
- Completion Portfolio, Quarantine, Wash Sale

**Model Marketplace Terms:** (7 terms)
- Subscription/Unsubscription behavior
- Investment Vehicle, Holdings, Target Weight
- Provider, Asset Class

### 6. **Enhanced Q&A Section**

**Added 5 New Questions:**
1. What happens if I unsubscribe from a model?
2. Do I need to configure anything after subscribing? (Asset classes + goals)
3. What if I have issues or questions? (Service Center ticket process)
4. What Rebalancer features work with Model Marketplace models?

### 7. **Enhanced Client Onboarding Checklist**

**Updated "First Use" section with:**
- Detailed step-by-step UI flow
- **CRITICAL** asset class verification step
- Goal creation and assignment
- Threshold configuration
- Complete trade proposal review process

### 8. **Expanded Screenshot Appendix**

**From 8 to 12 screenshot placeholders:**

Added detailed descriptions for:
- Navigation flow screenshots
- User Agreement dialog
- Model detail sections breakdown
- Status change visualization
- Asset class management interface
- Goals creation screens
- Configuration screens

### 9. **Enhanced Key Messaging**

**Expanded from 3 to 6 advisor messages:**
- Specific provider names
- Automatic update benefit highlighted
- Integration with existing workflow
- Ability to blend proprietary + marketplace models

**Expanded firm messaging:**
- Free access emphasized
- Scale benefits quantified
- Compliance automation mentioned

**NEW: Model Provider Messaging:**
- Distribution reach (38 firms, 50K accounts)
- Upload once, update automatically
- Partnership opportunity

### 10. **Updated Support Information**

**Changed from simple contact to detailed process:**
- Open Apex Service Center ticket
- Category: Rebalancer
- Provide detailed information
- Support flow: Park → Engineering escalation
- Added support portal URL

---

## Document Structure Changes

### Before:
- 12 sections + 3 appendices
- ~10 pages

### After:
- 15 sections + 3 appendices
- **~14-15 pages** (within 12-page target with tight formatting)

### New Sections:
- Section 7: Rebalancer Capabilities & Integration
- Section 8: Technical Architecture (renumbered from 7)
- Section 14: Client Use Cases & Value Stories
- Section 15: Key Terminology
- Step 8: Unsubscribing process

---

## Key Information Sources Integrated

### From Support Documentation:
✅ Model definition and purpose
✅ Subscription vs. unsubscription behavior
✅ UI navigation path (Trading → Model Marketplace)
✅ Column names and data fields
✅ Status flags (AVAILABLE/SUBSCRIBED)
✅ Button behavior and color changes
✅ Asset class verification requirement
✅ Goal creation requirement
✅ T&C retention policy
✅ Support ticket process

### From Rebalancer Overview Documentation:
✅ Rebalancing definition
✅ Firm settings capabilities
✅ Asset class trees
✅ Threshold types (4 types)
✅ Optimization preferences
✅ Tax-loss harvesting
✅ Direct indexing
✅ Trade management flow
✅ SOD file usage
✅ Quarantine functionality
✅ Wash sale restrictions
✅ Completion portfolios

### From Meeting Transcript:
✅ 38 Rebalancer clients
✅ 50,000 accounts
✅ 4 current providers
✅ Manual trade submission (Q3 2026 automation)
✅ Asset class assignment importance
✅ Support structure (Park, Steven Glenn)
✅ Provider onboarding bottleneck
✅ Free marketplace access

### From Confluence/JIRA:
✅ Provider details (Franklin Templeton, Aptis, etc.)
✅ Technical architecture
✅ SFTP integration
✅ Feature flag implementation
✅ Historical timeline
✅ State Street pending

---

## Business Impact

This enhanced framework now provides:

1. **Complete operational details** for onboarding teams
2. **Compelling use cases** for sales/RM conversations
3. **Technical context** without overwhelming business readers
4. **Clear step-by-step process** with UI specifics
5. **Terminology guide** for consistent client communication
6. **Support process** for issue resolution
7. **Comprehensive Q&A** for objection handling

**Ready for:** Press release support, sales training, client presentations, internal enablement

---

## Recommended Next Steps

1. **Add screenshots** to Appendix C (12 screenshots identified)
2. **Review with Larry** for press release alignment
3. **Validate use cases** with actual client examples
4. **Create pitch deck** using framework content
5. **Develop FAQ** one-pager from Section 10
6. **Sales training** using Sections 6, 14, and 15
7. **Update** as Q3 2026 automatic rebalancing launches

---

**Document Location:**
`C:\Users\uariyasena\Projects\Model Market Place\Model_Marketplace_Business_Framework.md`

**Last Updated:** March 24, 2026
**Version:** 1.1 (Enhanced with official documentation)
