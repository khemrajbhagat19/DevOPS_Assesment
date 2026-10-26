
import unittest
from pathlib import Path
from html.parser import HTMLParser


PROJECT_ROOT = Path(__file__).resolve().parent.parent
HTML_FILE = PROJECT_ROOT / "index.html"


class RegistrationHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms = []
        self.inputs = []
        self.selects = []
        self.buttons = []
        self.labels = []
        self.current_form = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.forms.append(attrs)
            self.current_form = True

        elif self.current_form and tag == "input":
            self.inputs.append(attrs)

        elif self.current_form and tag == "select":
            self.selects.append(attrs)

        elif self.current_form and tag == "button":
            self.buttons.append(attrs)

        elif self.current_form and tag == "label":
            self.labels.append(attrs)

    def handle_endtag(self, tag):
        if tag == "form":
            self.current_form = False


class TestStudentRegistrationForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        assert HTML_FILE.is_file(), "index.html was not found"

        cls.html = HTML_FILE.read_text(encoding="utf-8")
        cls.parser = RegistrationHTMLParser()
        cls.parser.feed(cls.html)

    def test_registration_form_exists(self):
        self.assertTrue(
            any(f.get("id") == "registrationForm"
                for f in self.parser.forms),
            "Registration form is missing"
        )

    def test_required_input_fields_exist(self):
        fields = {
            item.get("id"): item
            for item in self.parser.inputs
        }

        for field in ("studentName", "rollNumber", "email"):
            with self.subTest(field=field):
                self.assertIn(field, fields)
                self.assertIn("required", fields[field])

    def test_email_field_has_email_type(self):
        email = next(
            (item for item in self.parser.inputs
             if item.get("id") == "email"),
            None
        )
        self.assertIsNotNone(email)
        self.assertEqual(email.get("type"), "email")

    def test_course_dropdown_exists(self):
        self.assertTrue(
            any(item.get("id") == "course"
                for item in self.parser.selects),
            "Course dropdown is missing"
        )

    def test_submit_button_exists(self):
        self.assertTrue(
            any(item.get("type") == "submit"
                for item in self.parser.buttons),
            "Submit button is missing"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
