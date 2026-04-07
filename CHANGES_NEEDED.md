# Model Marketplace Framework - Changes Based on Steven's Feedback

## Date: April 1, 2026
## Reviewer: Steven Glenn (Engineering)

---

## 🚨 CRITICAL CHANGES (Must Fix Immediately)

### 1. REMOVE ALL Automatic Rebalancing References
**Why:** Feature doesn't exist yet, don't want to create false expectations
**Location:** Multiple places throughout app
- Line 318: Roadmap chart
- Line 600-602: "Coming in Q3 2026" box on Home page  
- Line 1086: KEY LIMITATION warning
- Line 2137: Q&A section
- Line 2449-2450: Roadmap timeline card
- Line 2486: Tab labels
- Line 2545: Section heading
- Line 2557: "Top Priority" text
- Line 2575: Expander section

**Action:** Remove Q3 2026 timeline and automatic rebalancing feature mentions entirely

---

### 2. FIX PRICING SECTION - Cannot Say "$0 FREE"
**Why:** Pricing varies by client type and usage, not actually free
**Current:** Shows "$0 Client Cost (FREE!)"
**New:** Show actual fee structure from screenshot:

**Rebalancer Fees:**
- 3 BPS of AUM assigned to rebalancing goal (annual, billed monthly)
- $0.20 per funded account per month

**Direct Indexing:**
- 3 BPS of AUM for standard direct indexing
- 6 BPS of AUM for custom direct indexing

**Locations:**
- Line 500-501: Hero section stat
- Line 1328: Revenue section
- Line 1338: Revenue section  
- Line 2134: Q&A answer

**Action:** Replace with "Contact your RM for pricing" or show actual fee structure

---

### 3. UPDATE ACCOUNT NUMBERS
**Why:** More than 50K accounts on platform
**Current:** "~50K accounts"
**Action:** Get exact number from Steven via Slack, or keep vague like "50,000+ accounts"

**Locations:**
- Line 468: Hero stat
- Line 824: Key metrics
- Line 1396: Messaging
- Line 1543: Distribution reach
- Line 1738: Scale metric
- Line 1829: Accounts metric

---

### 4. ADD "Accepted Proposals" Step in Rebalancer Flow
**Why:** Missing critical step between proposal generation and trade submission
**Current Flow:** Proposals → Submit Trades
**New Flow:** Proposals → Accept Proposals → Review → Submit Trades

**Action:** Add step showing accepted proposals review page

---

## 📝 MEDIUM PRIORITY CHANGES

### 5. Remove Specific Employee Contact Information
**Why:** Don't want client emails going to wrong people, employees might leave
**Location:** Contact Directory page
**Action:** Use generic contacts only:
- Client Service: "Submit ticket in Service Center"
- Onboarding: Generic team email or RM contact
- NO individual employee emails

---

### 6. Change Roadmap Dates to "Coming Soon"
**Why:** Don't want hard commitments on timelines that might change
**Location:** Roadmap page
**Current:** Q2 2026, Q3 2026, Q4 2026
**New:** "In Progress", "Coming Soon", "Future"

---

### 7. Simplify Rebalancer Capabilities Section
**Changes needed:**
- Remove "min trade size constraints" from firm level settings
- Move "threshold management" to position #2
- Move "Advanced Features" content under "Client and Investor Settings"

---

### 8. Clarify Unsubscribe Flow
**Issue:** Steven doesn't know what happens when you unsubscribe
**Action:** Mark as "TO BE CONFIRMED" and follow up with Nima/James

---

## ✅ THINGS THAT ARE CORRECT (No Changes Needed)

1. **Model Providers:** Aptis, Franklin Templeton, Timco and Sachs, State Street (coming soon) ✓
2. **38 Rebalancer Clients** ✓
3. **Client Eligibility Requirements** (must be Ascend client) ✓
4. **8-Step Process Flow** (overall structure is good) ✓
5. **Use Cases section** ✓
6. **Q&As from knowledge base** ✓

---

## 📋 TO DO - Follow Up Items

1. **Get exact KPIs from Steven via Slack:**
   - Exact number of accounts
   - Number of clients onboarding (Titan, Facet, Range, Mission Square)

2. **Get fee structure details from Steve Zushin** ✓ (DONE - have screenshot)

3. **Confirm with James/Nima:**
   - Who owns Model Marketplace
   - Unsubscribe flow details
   - Whether MM shows holdings and target weights

4. **Request Model Marketplace Access:**
   - Via #ascendoff Slack channel
   - Need to test full flow personally

5. **Get future roadmap from Nima:**
   - What features are actually coming
   - Can use "Coming Soon" language

---

## 🎯 WORD DOC CHANGES

Apply same changes to Word document:
1. Remove automatic rebalancing references
2. Update pricing section with actual fee structure
3. Remove Q3 2026 timelines
4. Add "Accepted Proposals" step
5. Remove employee contact info
6. Change dates to "Coming Soon"

---

## 📞 CONTACTS FOR QUESTIONS

- **KPIs & Metrics:** Steven Glenn
- **Pricing/Fees:** Steve Zushin  
- **Model Marketplace Ownership:** James Strataco / Nima Raphael
- **Future Roadmap:** Nima Raphael
- **Model Marketplace Access:** #ascendoff Slack channel
