# Model Marketplace Business Framework
**For Client Engagement & Onboarding**

---

## Executive Summary

**What is Model Marketplace?**
Model Marketplace is Apex's investment model distribution platform integrated within Ascend Rebalancer, allowing advisors to subscribe to professionally managed models from leading investment management providers. Models generate trade proposals based on market activity that realign investment portfolios according to a defined set of holdings and their weight. Subscribed models receive automatic updates and adjustments from the provider, enabling efficient model updates, allocation changes, and compliance monitoring.

**Key Value Proposition:**
- Access to institutional-grade investment models from top providers
- **Automatic updates** from providers when models are rebalanced or adjusted
- Seamless integration with Apex Rebalancer for portfolio construction and ongoing management
- Simplified subscription and implementation process
- No subscription fees for clients (free access to marketplace)
- Available models support efficient portfolio management with automatic weight adjustments

**Current Providers:**
- Aptis
- Franklin Templeton
- Timco and Sachs
- State Street (coming soon)

---

## 1. Client Eligibility & Prerequisites

### **Who Can Use Model Marketplace?**

✅ **Required:**
- Must be an **Ascend client** (not available on Classic platform)
- Must be an **active Rebalancer client**
- Correspondent must be configured for Model Marketplace access

❌ **Not Eligible:**
- Classic platform clients (until Ascend migration complete)
- Non-Rebalancer clients
- Clients mid-migration (unless willing to rebalance partial accounts)

### **Current Market Size**
- 38 active Rebalancer clients
- ~50,000 accounts currently utilizing Rebalancer
- All are potential Model Marketplace users

---

## 2. The Model Marketplace Process Flow

### **Step 1: Initial Access Setup**
**WHO:** Apex Onboarding Team / Client Configurator Team
**WHAT:** Enable Model Marketplace at correspondent level
**WHERE:** Client Configurator → Experience Settings → Enable Model Marketplace

**Timeline:** Completed during client onboarding

---

### **Step 2: User Permission Configuration**
**WHO:** Client Administrator / Apex Client Services
**WHAT:** Grant subscribe permissions to specific users
**WHY:** Not all users should have subscription authority

**Access Levels:**
- **View Access:** All correspondent users can browse models, view holdings, details
- **Subscribe Access:** Limited to authorized users only (requires explicit permission)

---

### **Step 3: Client Acceptance & Discovery**
**WHO:** End Client/Advisor
**WHAT:**
1. Sign in to Ascend Workstation
2. Find the main menu and open the **Trading** section
3. Select **Model Marketplace** in left navigation
4. On first visit: Accept **Apex User Agreement/Terms & Conditions** (one-time, applies to all providers)
5. Browse available models using sortable columns:
   - Provider
   - Model
   - Investment Vehicle
   - Status (AVAILABLE or SUBSCRIBED)

**Duration:** 5-10 minutes (one-time setup)

**Important:** Your agreement to Apex T&Cs is retained even if you later unsubscribe from models

---

### **Step 4: Model Evaluation**
**WHO:** Client/Advisor
**WHAT:** Select a model name to view detailed information:

**Holdings Section:**
- Symbol (securities in the model)
- Target Weight (allocation percentages)

**Summary Section:**
- Provider name
- Investment Vehicle type
- Inception Date
- Last Updated date

**Resources Section:**
- Model Fact Sheet (PDF/link)
- Provider Website

**Decision Point:** Review information to determine if the model aligns with account goals and investment strategy

---

### **Step 5: Model Subscription**
**WHO:** Authorized Client User (with subscribe permission)
**WHAT:**
1. Click green **Subscribe** button on selected model
2. Accept **Provider-Specific Terms & Conditions** (one-time per provider)
   - Terms retained even if you later unsubscribe
3. Confirm subscription

**Results:**
- Status flag changes from **AVAILABLE** to **SUBSCRIBED**
- Subscribe button changes from green to red **Unsubscribe** button
- Success message displays
- Model immediately appears in Rebalancer settings

**Subscription Benefit:** Model receives automatic updates and adjustments from the investment management provider

---

### **Step 6: Post-Subscription Configuration in Rebalancer**
**WHO:** Client/Advisor
**WHAT:**

**6a. Verify Asset Class Assignments (CRITICAL)**
1. Sign in to Rebalancer
2. Navigate to asset class management
3. Ensure each component security in the subscribed model is assigned to the appropriate asset class
   - Example: SPDR Gold Trust (GLD) should be assigned to Commodity asset class
4. This ensures optimum Rebalancer performance
   - **Reference:** "Manage Asset Classes in Rebalancer" documentation

**6b. Create and Assign Goals**
1. Navigate to Rebalancer → Settings → Models
2. View subscribed Model Marketplace models alongside custom models
3. Create goals using the subscribed model
4. Assign model to fund account goals
   - **Reference:** "Create and Fund Goals in Rebalancer" documentation
5. Configure rebalancing parameters (thresholds, optimization preferences)

---

### **Step 7: Portfolio Rebalancing**
**WHO:** Client/Advisor
**WHAT:**
1. Initiate rebalance (manual trigger or API call)
2. Review generated buy/sell orders
3. Review compliance disclosures
4. Submit trades for execution

**KEY LIMITATION:** Apex does NOT automatically execute trades (Q3 2026 roadmap item)

**Current Process:** Client must review and submit all trade orders

---

### **Step 8: Unsubscribing from Models (Optional)**

**Important Behavior:**
- Unsubscribing **deactivates automatic updates** from the investment management provider
- Holdings and weights from the last subscription remain **implemented and active**
- Model continues to allocate at the last subscribed weight

**Example:**
- Subscribed model is set to: XXX=80%, ZZZ=20%
- Provider updates model to: XXX=70%, ZZZ=30%
- If you unsubscribe before the update, your portfolio remains at 80/20
- The 70/30 update is **not** applied

**To Fully Discontinue Use:**
- Unsubscribing alone is NOT sufficient
- Must **delete the model** from Rebalancer
- **Reference:** "Deleting a Model" section in "Create and Manage Models in Rebalancer"

**Terms & Conditions:**
- Your acceptance of Apex T&Cs and Provider T&Cs is **retained** even after unsubscribing
- You can re-subscribe without accepting T&Cs again

---

## 3. Roles & Responsibilities Matrix

| Activity | Client | Apex RM/Sales | Apex Onboarding | Apex Client Services | Engineering/PM |
|----------|--------|---------------|-----------------|---------------------|----------------|
| **Pre-Sales & Discovery** |
| Identify Rebalancer prospects | ○ | ● | ○ | | |
| Present Model Marketplace value | | ● | ● | | |
| Validate Ascend migration status | | ● | ● | | |
| **Onboarding** |
| Enable Model Marketplace (Client Configurator) | | | ● | | |
| Configure user subscribe permissions | ● | | ● | ○ | |
| Provide training/documentation | | ○ | ● | ○ | |
| **Ongoing Usage** |
| Accept Apex T&Cs | ● | | | | |
| Browse and evaluate models | ● | | | | |
| Subscribe to models | ● | | | | |
| Assign models to accounts | ● | | | | |
| Initiate rebalancing | ● | | | | |
| Submit trade orders | ● | | | | |
| **Support** |
| Handle usage questions | | | | ● | ○ |
| Troubleshoot technical issues | | | | ● | ● |
| Bug fixes and enhancements | | | | | ● |

**Legend:** ● = Primary Owner | ○ = Supporting Role

---

## 4. Model Provider Onboarding Process

### **Adding New Model Providers to Marketplace**

**WHO DRIVES:** Apex Business Development / Product Team
**CURRENT CONTACT:** Rich or Larry (taking over from previous lead)

**Process Steps:**

1. **Sourcing & Outreach**
   - Identify potential model providers
   - Initial business discussions
   - Validate provider credibility and model quality

2. **Legal & Compliance**
   - Contract negotiation
   - Provider terms & conditions review
   - Compliance approval
   - **CURRENT BOTTLENECK:** No dedicated resource for this process

3. **Technical Integration**
   - Provider submits model holdings data
   - Data format validation (holdings, weights, metadata)
   - SFTP setup if required (for ongoing updates)
   - Example: Franklin Templeton daily ETF performance reporting

4. **Testing & Validation**
   - UAT environment testing
   - Data accuracy verification
   - User acceptance testing

5. **Go-Live**
   - Upload models to production
   - Provider models appear in marketplace
   - Internal announcement to sales team

**Timeline:** Varies (State Street awaiting holdings data)

---

## 5. Revenue Model & Pricing Strategy

### **Current State (2026)**
- **Client Fees:** $0 (Free access to Model Marketplace)
- **Provider Fees:** $0 (No charges currently)
- **Revenue Source:** Indirect (custody fees, Rebalancer subscription)

### **Future State Recommendations**

**Option A: Charge Model Providers**
- Marketplace listing fees
- Based on precedent (Etsy, Facebook Marketplace model)
- Providers pay for distribution access
- **Rationale:** Once marketplace gains adoption, providers gain value from client access

**Option B: Tiered Client Pricing**
- Free tier: Limited provider access
- Premium tier: Full provider catalog
- **Challenge:** Limited current adoption makes this difficult

**Option C: Hybrid Model**
- Free for clients
- Revenue share with providers on AUM or usage
- Platform fees for premium providers

**Recommended Approach:** Wait for marketplace adoption, then implement provider fees (Q4 2026+)

---

## 6. Client Communication & Marketing Strategy

### **Target Audience: Current Rebalancer Clients**
**Priority 1:** 38 existing Rebalancer clients on Ascend
**Priority 2:** Classic clients post-Ascend migration
**Priority 3:** New Rebalancer prospects

### **Key Messaging**

**For Advisors:**
- "Access institutional-quality investment models from Franklin Templeton, Aptis, Timco and Sachs, and State Street"
- "Models automatically update when providers rebalance—no manual intervention required"
- "Reduce time spent on portfolio construction by 70% while maintaining quality"
- "Seamlessly integrate with your existing Apex Rebalancer workflow"
- "Combine marketplace models with your proprietary strategies for client customization"
- "Full tax-loss harvesting and optimization across all models"

**For Firms:**
- "Launch or expand managed portfolios without hiring an investment team"
- "Scale to thousands of accounts with automated model updates and rebalancing"
- "Free access to Model Marketplace for all Rebalancer clients"
- "Compete with larger firms by offering institutional-grade models"
- "Choose from multiple providers to match your firm's investment philosophy"
- "Maintain compliance with automatic provider updates and built-in monitoring"

**For Model Providers:**
- "Distribute your models to 38 RIA firms managing 50,000+ accounts"
- "Automated delivery platform—upload once, update automatically"
- "Reach Apex's growing ecosystem of digital advisors and wealth managers"
- "Partnership opportunity with premier fintech custody platform"

### **Communication Channels**

1. **Direct Outreach**
   - RM/Sales team to existing Rebalancer clients
   - Email campaign highlighting providers and models
   - One-on-one demos

2. **Documentation & Resources**
   - Developer portal documentation (already exists)
   - This framework document
   - Video tutorials (recommended)
   - Provider fact sheets

3. **Press Release** (Pending Framework Completion)
   - Announce Model Marketplace availability
   - Highlight provider partnerships
   - Include client testimonials (if available)

4. **Internal Enablement**
   - Sales team training on Model Marketplace
   - RM playbook for client conversations
   - FAQ document for common objections

---

## 7. Rebalancer Capabilities & Integration

### **What is Apex Rebalancer?**

Rebalancing is the process of adjusting a portfolio's asset allocations to align with levels advisors specify in an investment plan. Apex's Rebalancer allows advisors to manage portfolios based on asset types, expected returns, and risk levels. The Rebalancer creates trade proposals that realign investment portfolios to targets and ranges that match the desired portfolio models as markets move and asset values shift.

**Model Marketplace Integration:** Subscribed models from the marketplace become available in Rebalancer for portfolio construction, rebalancing proposals, and ongoing management.

### **Key Rebalancer Features That Enhance Model Marketplace**

**1. Firm-Level Settings**
- Minimum trade size (minimum dollar value for trade execution)
- Trade-off preferences between drift reduction and tax sensitivity
- Tax-loss harvesting configuration
- Organization-wide API keys and user management

**2. Asset Class Management**
- Create asset class trees (equities, fixed income, mutual funds, commodities, etc.)
- Map securities to appropriate asset classes
- **CRITICAL:** All securities in Model Marketplace models must be mapped for proper functioning

**3. Models, Frameworks & Goals**
- Custom models created in-house
- Model Marketplace subscribed models
- Frameworks for goal-based investing automation
- Goals assigned to individual client accounts
- Direct indexing for index replication with customization

**4. Threshold Management**
- Four threshold types: asset class, securities, model target cash, mandatory cash
- Absolute and relative difference percentages
- Upper/lower limit configurations
- Filter accounts that exceed drift limitations

**5. Client & Investor Settings**
- Security restrictions (add/lift restrictions)
- Wash sale restrictions handling
- Optimization preferences (drift vs. tax sensitivity)
- Tax-loss harvesting enablement
- Minimum cash settings
- Account liquidation capabilities
- Account quarantine (manual or automatic)

**6. Direct Indexing**
- Replicate index fund performance with individual security ownership
- Portfolio customization and stock exclusions
- Tax-loss harvesting optimization
- Custom index allocations

**7. Trade Management**
- Generate trade proposals from start-of-day (SOD) files
- Review and submit trades
- Trade blotter for executed trade analysis
- Historical trade exploration and download
- Fill quantity and price tracking

**8. Advanced Features**
- Completion portfolios for restricted security drift reduction
- Cash generation via minimum cash parameter
- Position liquidation
- Wash sale restriction management
- Compliance monitoring

---

## 8. Technical Architecture Overview (For Business Context)

### **Platform Components**

```
Client Browser (Ascend Workstation)
          ↓
Model Marketplace UI (Ascend)
          ↓
Apex GraphQL Gateway (apex-grql)
          ↓
Model Marketplace Service (MMP)
          ↓
Rebalancer API (AdvisorArch)
          ↓
Model Data & Holdings
```

### **Key Integration Points**

1. **Client Configurator:** Controls correspondent-level access
2. **User Permissions:** Controls subscribe access per user
3. **Rebalancer:** Receives subscribed models automatically
4. **SFTP:** Provider data feeds (Franklin Templeton daily updates)

### **Monitoring & Support**

- **24/7 Monitoring:** Slack alerts for service issues
- **Start-of-Day Files:** Automated monitoring for data freshness
- **PagerDuty:** Escalation for production and sandbox issues
- **Client Service Tickets:** Tracked through standard support flow
- **Current Support Staff:** Park (primary), backed by Steven Glenn

---

## 9. Client Onboarding Checklist

### **Pre-Onboarding**
- [ ] Confirm client is Rebalancer customer
- [ ] Confirm client is on Ascend (not Classic)
- [ ] If mid-migration, confirm client acceptance of partial rebalancing
- [ ] Identify which users need subscribe permissions

### **Technical Setup**
- [ ] Onboarding team enables Model Marketplace in Client Configurator
- [ ] Configure subscribe permissions for authorized users
- [ ] Validate access in Ascend environment

### **Client Enablement**
- [ ] Share Model Marketplace documentation
- [ ] Provide this framework document
- [ ] Schedule walkthrough/demo (if needed)
- [ ] Share provider fact sheets

### **First Use**
- [ ] Client accepts Apex T&Cs (User Agreement)
- [ ] Client browses available models (sort/search by Provider, Model, Investment Vehicle, Status)
- [ ] Client reviews model details (holdings, weights, summary, resources)
- [ ] Client subscribes to first model
- [ ] Accept provider-specific T&Cs
- [ ] Verify status changes to SUBSCRIBED
- [ ] **CRITICAL:** Verify each security in model is assigned to correct asset class in Rebalancer
- [ ] Create goals using subscribed model
- [ ] Assign model to fund goals in test account
- [ ] Configure thresholds and optimization preferences
- [ ] Execute test rebalance
- [ ] Review trade proposals
- [ ] Submit trade orders

### **Go-Live**
- [ ] Roll out to additional users/accounts
- [ ] Monitor for issues in first 30 days
- [ ] Collect feedback for improvements

---

## 10. Common Questions & Objections

### **Q: What if we're still on Classic?**
**A:** Model Marketplace is Ascend-only. Let's discuss your Ascend migration timeline and prioritize Model Marketplace access post-migration.

### **Q: We're not Rebalancer clients. Can we still use Model Marketplace?**
**A:** No, Model Marketplace requires Rebalancer subscription. Let's explore if Rebalancer is right for your firm first.

### **Q: Do we have to pay for Model Marketplace?**
**A:** No, access is currently free for all Rebalancer clients. You only pay the standard fees embedded in the ETFs/securities within the models.

### **Q: Can we customize the models after subscribing?**
**A:** Subscribed models from providers cannot be edited, but you can create custom models in Rebalancer and use marketplace models as a starting point/reference.

### **Q: How often are models updated?**
**A:** Providers update their models on their own schedule. Franklin Templeton provides daily performance reporting. Model composition updates vary by provider.

### **Q: Does Apex automatically rebalance our accounts?**
**A:** Not currently. You must manually initiate rebalancing or call our API. Automatic scheduled rebalancing is planned for Q3 2026.

### **Q: What if we want a specific provider added?**
**A:** Contact your RM. We're actively seeking new provider partnerships (current bottleneck: no dedicated BD resource).

### **Q: Are there regulatory/compliance concerns?**
**A:** Each provider has their own T&Cs that clients accept. Apex provides disclosure language on all trade orders. Clients maintain full responsibility for trade execution.

### **Q: What happens if a model provider leaves the marketplace?**
**A:** You would be notified in advance. Already-assigned accounts would continue with the last known model composition, but new subscriptions would not be available.

### **Q: What happens if I unsubscribe from a model?**
**A:** Unsubscribing stops automatic updates from the provider, but your portfolios continue using the last subscribed weights. To fully discontinue, you must delete the model from Rebalancer. Your T&C acceptance is retained for future re-subscription.

### **Q: Do I need to configure anything after subscribing?**
**A:** Yes, two critical steps: (1) Verify each security in the model is assigned to the correct asset class in Rebalancer for optimal performance, and (2) Create goals and assign the model to fund those goals in your client accounts.

### **Q: What if I have issues or questions?**
**A:** Open an Apex Service Center ticket and navigate to the Rebalancer category. Provide as much detail as possible about your issue. Support is handled by Park (primary) with engineering escalation available.

### **Q: What Rebalancer features work with Model Marketplace models?**
**A:** All standard Rebalancer features apply: firm settings, thresholds, tax-loss harvesting, optimization between drift reduction and tax sensitivity, direct indexing, asset class management, and trade blotter analysis.

---

## 11. Success Metrics & KPIs

### **Adoption Metrics**
- Number of correspondents with Model Marketplace enabled
- Number of users with subscribe permissions
- Number of active model subscriptions
- Number of accounts utilizing marketplace models
- Subscription conversion rate (browsers → subscribers)

### **Usage Metrics**
- Models subscribed per client (average)
- Most popular providers
- Most popular models
- Rebalance frequency using marketplace models
- AUM in marketplace-model-based accounts

### **Business Impact**
- Incremental AUM from Model Marketplace clients
- Client retention rate (marketplace users vs. non-users)
- Time-to-value for new Rebalancer clients
- NPS for marketplace users

### **Current Baseline (March 2026)**
- Live clients using Rebalancer: 38
- Accounts on Rebalancer: ~50,000
- Model providers: 4 (Aptis, Franklin Templeton, Timco and Sachs)
- Known marketplace users: Public, plus others (specific count TBD)

---

## 12. Roadmap & Future Enhancements

### **Q2 2026 (Current Focus)**
- Onboard Titan, Range Finance, and other new Rebalancer clients
- Add State Street models (pending holdings data)
- Stabilize current functionality
- Marketing launch and press release

### **Q3 2026 (Planned)**
- **Automatic Scheduled Rebalancing** (Top Priority)
  - Clients configure rebalance frequency (daily, weekly, monthly, quarterly)
  - System automatically generates orders
  - Still requires client review before execution
- Enhanced provider onboarding process
- Dedicated BD resource for provider acquisition

### **Q4 2026 & Beyond (Roadmap)**
- Revenue model implementation (provider fees)
- Expanded provider catalog (target: 10+ providers)
- Model performance analytics dashboard
- Advanced filtering and search
- Model comparison tools
- Automated trade execution (pending compliance approval)

---

## 13. Next Steps & Action Items

### **For Apex Sales/RM Team**
1. Review this framework and provide feedback
2. Identify top 10 Rebalancer clients for Model Marketplace outreach
3. Schedule training session on Model Marketplace positioning
4. Develop client pitch deck using this framework

### **For Apex Marketing**
1. Finalize press release using this framework
2. Create visual assets (screenshots, diagrams, videos)
3. Develop email campaign for Rebalancer client base
4. Coordinate with Provider Relations on joint marketing

### **For Apex Product/Engineering**
1. Prioritize automatic rebalancing for Q3 2026
2. Assign dedicated resource for provider BD and onboarding
3. Enhance documentation with client screenshots
4. Implement usage analytics dashboard

### **For Prospects/Clients**
1. Validate eligibility (Ascend + Rebalancer)
2. Review provider and model catalog
3. Schedule demo with RM
4. Submit onboarding request

---

## 14. Client Use Cases & Value Stories

### **Use Case 1: RIA Scaling Portfolio Management**

**Client Profile:** Mid-sized RIA with 500 client accounts, limited in-house investment research team

**Challenge:** Advisors spend 15+ hours weekly constructing and maintaining custom portfolios, limiting client acquisition capacity

**Solution with Model Marketplace:**
1. Subscribe to Franklin Templeton and Aptis ETF models aligned with firm's investment philosophy
2. Create goal-based frameworks using marketplace models (conservative, balanced, growth)
3. Assign models to client segments based on risk tolerance and objectives
4. Rebalancer generates trade proposals automatically as markets drift
5. Marketplace models receive automatic provider updates (no manual rebalancing needed)

**Results:**
- 70% reduction in portfolio construction time
- Consistent investment quality across all accounts
- Scalable to 1000+ accounts without additional investment staff
- Tax-loss harvesting and optimization built-in

---

### **Use Case 2: Digital Advisor Launching New Product**

**Client Profile:** Digital investment platform adding managed portfolios to self-directed offering

**Challenge:** Need institutional-quality models quickly without building in-house model management team

**Solution with Model Marketplace:**
1. Subscribe to multiple provider models across risk spectrums
2. White-label models as platform investment strategies
3. Use Rebalancer API to automate account rebalancing
4. Leverage direct indexing for tax-optimized versions

**Results:**
- Launch managed portfolios in weeks vs. months
- Professional-grade investment models with automatic updates
- Scalable to 50,000+ accounts
- Differentiated tax optimization features

---

### **Use Case 3: Existing Rebalancer Client Enhancing Offering**

**Client Profile:** Wealth management firm already using Apex Rebalancer with custom models

**Challenge:** Clients requesting access to specific institutional strategies (e.g., thematic ETFs, ESG models)

**Solution with Model Marketplace:**
1. Subscribe to complementary marketplace models alongside existing custom models
2. Create blended goals using both custom and marketplace models
3. Offer clients choice between proprietary and third-party strategies
4. Use asset class management to optimize across all models

**Results:**
- Expanded investment menu without research overhead
- Client retention through broader product suite
- Flexibility to compete with larger firms
- Maintained use of proprietary models where differentiated

---

### **Use Case 4: Sub-Advisory Relationship**

**Client Profile:** Large asset manager (like Voya Investment Management) distributing models to advisor network

**Challenge:** Need scalable distribution platform for model portfolios to reach more advisors

**Solution with Model Marketplace:**
1. Partner with Apex as Model Marketplace provider
2. Upload model portfolios to marketplace
3. Apex advisors subscribe and implement across client accounts
4. Provider updates models as market conditions change
5. Automatic propagation to all subscribed accounts

**Results:**
- Distribution to 38 RIA firms and 50,000+ accounts
- Automated model updates across entire advisor network
- Reduced operational burden of individual advisor feeds
- Analytics on model adoption and usage

---

## 15. Key Terminology for Client Conversations

### **Rebalancer Terms**

**Rebalancing:** The process of adjusting a portfolio's asset allocations to align with specified levels in an investment plan, compensating for market movements and asset value shifts.

**Models:** Defined sets of holdings and their target weights that guide portfolio construction. Models can be:
- Custom-created in Rebalancer
- Subscribed from Model Marketplace providers
- Direct indexes

**Frameworks:** Automation tools for goal-based investing practices.

**Goals:** Building blocks assigned to individual accounts to guide rebalancing. Created from models and frameworks.

**Start-of-Day (SOD) Files:** Daily position data files that the Rebalancer uses to generate trade proposals.

**Trade Proposals:** Recommended buy/sell orders generated by the Rebalancer to realign portfolios with target models.

**Drift:** The deviation between current portfolio allocations and target model weights due to market movements.

**Thresholds:** Parameters that filter which accounts to trade based on how far they've drifted from targets.

**Optimization:** The balance preference between drift reduction and tax sensitivity when generating trade proposals.

**Tax-Loss Harvesting:** Strategy to sell securities at a loss to offset capital gains, improving after-tax returns.

**Direct Indexing:** Owning individual securities that replicate an index rather than buying an index fund, enabling customization and tax optimization.

**Completion Portfolio:** Technique to reduce drift in portfolios with restricted securities.

**Quarantine:** Status preventing the Rebalancer from generating proposals for an account (automatic for restricted accounts or manual).

**Wash Sale:** IRS rule preventing claiming tax losses on securities repurchased within 30 days; Rebalancer manages these restrictions.

### **Model Marketplace Terms**

**Subscription:** Active connection to a model provider that enables automatic updates when the provider adjusts the model.

**Unsubscription:** Deactivating automatic updates while retaining the last known model weights.

**Investment Vehicle:** The type of securities used in a model (e.g., ETFs, mutual funds, individual securities).

**Holdings:** The specific securities (symbols) that comprise a model.

**Target Weight:** The percentage allocation for each security in a model.

**Provider:** The investment management firm offering models on the marketplace (Aptis, Franklin Templeton, Timco and Sachs, State Street).

**Asset Class:** Category grouping for securities (equities, fixed income, commodities, etc.) used by the Rebalancer for optimization and analysis.

---

## Appendix A: Quick Reference Guide

**Access Model Marketplace:** Ascend Workstation → Model Marketplace (left nav)

**Prerequisites:**
- ✅ Ascend client
- ✅ Rebalancer client
- ✅ Correspondent enabled in Client Configurator
- ✅ User has subscribe permission (for subscribing)

**Two Sets of T&Cs:**
1. Apex T&Cs (one-time, all providers)
2. Provider T&Cs (one-time per provider)

**Cost:** Free

**Support:**
- Open Apex Service Center ticket
- Category: Rebalancer
- Provide detailed information about issue
- Primary: Park → Engineering escalation as needed

**Documentation:**
- Apex Support Portal: support.apexfintechsolutions.com
- Developer Portal
- This Framework

---

## Appendix B: Contact Directory

**Product Management:**
- Model Marketplace & Rebalancer PM: [Contact from transcript]

**Sales/RM Coordination:**
- Provider BD: Rich or Larry

**Onboarding:**
- Client Configurator Team: [Via standard onboarding process]

**Client Services:**
- Primary Support: Park
- Backup: Steven Glenn

**Technical Escalation:**
- Engineering: Via PagerDuty or Client Service escalation

**Provider Relations:**
- Franklin Templeton: Jennifer Zmarzly (Jennifer.Zmarzly@franklintempleton.com)

---

## Appendix C: Screenshots & Visual Aids

**[PLACEHOLDER: Screenshots to be inserted]**

### **Model Marketplace Flow**
1. **Ascend Workstation Home → Trading Section**
   - Show navigation to Model Marketplace

2. **First Visit: User Agreement Dialog**
   - Apex Terms & Conditions acceptance screen

3. **Model Marketplace Home Screen**
   - Grid view with columns: Provider, Model, Investment Vehicle, Status
   - Show sortable/searchable interface
   - Display mix of AVAILABLE and SUBSCRIBED status flags

4. **Model Detail Page**
   - Holdings section (Symbol, Target Weight)
   - Summary section (Provider, Investment Vehicle, Inception Date, Last Updated)
   - Resources section (Fact Sheet link, Website link)
   - Green Subscribe button (for AVAILABLE models)
   - Red Unsubscribe button (for SUBSCRIBED models)

5. **Provider Terms & Conditions Dialog**
   - Provider-specific T&C acceptance screen

6. **Subscription Success**
   - Status change from AVAILABLE to SUBSCRIBED
   - Button change from green Subscribe to red Unsubscribe
   - Success message

### **Rebalancer Integration**
7. **Rebalancer Settings → Models**
   - List showing both custom models and Model Marketplace subscribed models
   - Model type indicators

8. **Asset Class Management**
   - Security-to-asset-class mapping interface
   - Example: GLD assigned to Commodity class

9. **Goals Creation**
   - Creating goals with Model Marketplace models
   - Goal assignment to accounts

10. **Rebalance Proposals**
    - Generated buy/sell orders from Model Marketplace model
    - Compliance disclosures
    - Submit for trading button

### **Configuration**
11. **Client Configurator**
    - Experience Settings → Model Marketplace toggle

12. **User Permissions**
    - Subscribe permission configuration for users

---

**Document Version:** 1.0
**Last Updated:** March 24, 2026
**Owner:** Product Marketing / Business Development
**Review Cycle:** Quarterly or as material changes occur

---

*This framework is intended for internal Apex use and approved client/prospect sharing. Not for public distribution without Marketing approval.*
