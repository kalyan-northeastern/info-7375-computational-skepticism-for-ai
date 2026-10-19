#!/usr/bin/env python3
"""Tests for the connector rule in collect.py: both halves required, and the GSI role stays out."""
import json, os, unittest

import collect

KW = json.load(open(os.path.join(collect.HERE, "keywords.json")))


def view(title, text, company="Acme"):
    return {"company": company, "title": title, "text": text}


class ConnectorRule(unittest.TestCase):
    def test_account_role_naming_universities_is_kept_for_that_reason(self):
        m, _ = collect.judge(view("Strategic Partnerships Manager", "You will own relationships with universities."), KW)
        self.assertEqual(m["kept_because"], "account or partnership role whose body names higher education")
        self.assertEqual(m["connector"]["institution"], ["universities"])

    def test_adoption_and_marketing_roles_that_reach_universities_are_kept(self):
        for title in ("Customer Adoption Manager", "Solutions Marketing Lead, Public Sector", "Customer Success Manager"):
            m, _ = collect.judge(view(title, "You will drive adoption across universities and colleges."), KW)
            self.assertIsNotNone(m, title)
            self.assertEqual(m["kept_because"], "account or partnership role whose body names higher education", title)
            self.assertTrue(m["connector"]["institution"], title)

    def test_the_industry_account_executive_with_educate_boilerplate_stays_out(self):
        text = ("Navigate complex retail organisations to reach key decision-makers, educate them about our services, "
                "and help them succeed. Minimum education: a Bachelor's degree.")
        m, _ = collect.judge(view("Enterprise Account Executive - Retail", text, "Anthropic"), KW)
        self.assertIsNone(m)

    def test_title_half_alone_is_not_enough(self):
        m, why = collect.judge(view("Partner Account Manager", "You will own relationships with large consulting firms."), KW)
        self.assertIsNone(m)

    def test_body_half_alone_is_not_enough(self):
        m, _ = collect.judge(view("Software Engineer", "Our customers include universities."), KW)
        self.assertIsNone(m)

    def test_the_gsi_posting_that_prompted_the_rule_stays_out(self):
        text = ("Own our relationship with one or two of the world's largest global systems integrators, "
                "certification of 50,000 practitioners, a multi-year strategic agreement.")
        m, _ = collect.judge(view("Senior Partner Account Manager Global Systems Integrator Alliances", text, "Anthropic"), KW)
        self.assertIsNone(m)


if __name__ == "__main__":
    unittest.main()
