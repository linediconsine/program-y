import unittest

from programy.config import ConfigurationFactory, YamlConfigurationFile
import os

class ConfigurationFactoryTests(unittest.TestCase):

    def test_guess_format_from_filename(self):
        config_format = ConfigurationFactory.guess_format_from_filename("file.yaml")
        self.assertEqual(config_format, "yaml")
        config_format = ConfigurationFactory.guess_format_from_filename("file.json")
        self.assertEqual(config_format, "json")
        config_format = ConfigurationFactory.guess_format_from_filename("file.xml")
        self.assertEqual(config_format, "xml")

    def test_guess_format_no_extension(self):
        with self.assertRaises(Exception):
            ConfigurationFactory.guess_format_from_filename("file_yaml")

    def test_get_config_by_name(self):
        config_type = ConfigurationFactory.get_config_by_name("yaml")
        self.assertIsNotNone(config_type)
        config_type = ConfigurationFactory.get_config_by_name("json")
        self.assertIsNotNone(config_type)
        config_type = ConfigurationFactory.get_config_by_name("xml")
        self.assertIsNotNone(config_type)

    def test_get_config_by_name_wrong_extension(self):
        with self.assertRaises(Exception):
            ConfigurationFactory.get_config_by_name("other")
        with self.assertRaises(Exception):
            ConfigurationFactory.get_config_by_name("")
        with self.assertRaises(Exception):
            ConfigurationFactory.get_config_by_name(None)


class YamlConfigurationFileTests(unittest.TestCase):

    def test_load_from_file(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_file(os.path.dirname(__file__)+"/test_yaml.yaml", ",")
        self.assertIsNotNone(yaml.yaml_data)
        brain = yaml.get_section("brain")
        self.assertIsNotNone(brain)
        files = yaml.get_section("files", brain)
        self.assertIsNotNone(files)
        aiml = yaml.get_section("aiml", files)
        self.assertIsNotNone(aiml)

        files = yaml.get_section("files", aiml)
        self.assertIsNotNone(files)
        self.assertEqual(files, "/aiml")
        extension = yaml.get_section("extension", aiml)
        self.assertIsNotNone(extension)
        self.assertEqual(extension, ".aiml")
        directories = yaml.get_section("directories", aiml)
        self.assertIsNotNone(directories)
        self.assertEqual(directories, True)


class ClientConfigurationTests(unittest.TestCase):

    def test_load_config_data_yaml(self):
        config_data = ConfigurationFactory.load_configuration_from_file(os.path.dirname(__file__)+"/test_yaml.yaml")
        self.assert_config_data(config_data)

    def test_load_config_data_json(self):
        config_data = ConfigurationFactory.load_configuration_from_file(os.path.dirname(__file__)+"/test_json.json", None)
        self.assert_config_data(config_data)

    def test_load_config_data_xml(self):
        config_data = ConfigurationFactory.load_configuration_from_file(os.path.dirname(__file__)+"/test_xml.xml")
        self.assert_config_data(config_data)

    def assert_config_data(self, config_data):
        self.assertIsNotNone(config_data)

        self.assertIsNotNone(config_data.bot_configuration)
        self.assertEqual(config_data.bot_configuration.prompt, ">>>")
        self.assertEqual(config_data.bot_configuration.default_response, "Sorry, I don't have an answer for that!")
        self.assertEqual(config_data.bot_configuration.exit_response, "So long, and thanks for the fish!")

        self.assertIsNotNone(config_data.brain_configuration)
        self.assertIsNotNone(config_data.brain_configuration.aiml_files)
        self.assertEqual(config_data.brain_configuration.aiml_files.files, "/aiml")
        self.assertEqual(config_data.brain_configuration.aiml_files.extension, ".aiml")
        self.assertEqual(config_data.brain_configuration.aiml_files.directories, True)

        self.assertIsNotNone(config_data.brain_configuration.set_files)
        self.assertEqual(config_data.brain_configuration.set_files.files, "/sets")
        self.assertEqual(config_data.brain_configuration.set_files.extension, ".txt")
        self.assertEqual(config_data.brain_configuration.set_files.directories, False)

        self.assertIsNotNone(config_data.brain_configuration.map_files)
        self.assertEqual(config_data.brain_configuration.map_files.files, "/maps")
        self.assertEqual(config_data.brain_configuration.map_files.extension, ".txt")
        self.assertEqual(config_data.brain_configuration.map_files.directories, True)

        self.assertEqual(config_data.brain_configuration.denormal, "denormal.txt")
        self.assertEqual(config_data.brain_configuration.normal, "normal.txt")
        self.assertEqual(config_data.brain_configuration.gender, "gender.txt")
        self.assertEqual(config_data.brain_configuration.person2, "person2.txt")
        self.assertEqual(config_data.brain_configuration.predicates, "predicates.txt")
        self.assertEqual(config_data.brain_configuration.pronouns, "pronouns.txt")
        self.assertEqual(config_data.brain_configuration.properties, "properties.txt")
        self.assertEqual(config_data.brain_configuration.triples, "triples.txt")
        self.assertEqual(config_data.brain_configuration.preprocessors, "preprocessors.txt")

        self.assertIsNotNone(config_data.brain_configuration.services)
        self.assertEqual(4, len(config_data.brain_configuration.services))

        self.assertIn(config_data.brain_configuration.services[0].name, ["REST", "PANNOUS", "PANDORA", "WIKIPEDIA"])
        self.assertIn(config_data.brain_configuration.services[0].path, ["programy.utils.services.rest.GenericRESTService",
                                                                         "programy.utils.services.pannous.PannousService",
                                                                         "programy.utils.services.pandora.PandoraService",
                                                                         "programy.utils.services.google.GoogleService",
                                                                         "programy.utils.services.wikipedia.WikipediaService"])

        self.assertIn(config_data.brain_configuration.services[1].name, ["REST", "PANNOUS", "PANDORA", "WIKIPEDIA"])
        self.assertIn(config_data.brain_configuration.services[1].path, ["programy.utils.services.rest.GenericRESTService",
                                                                         "programy.utils.services.pannous.PannousService",
                                                                         "programy.utils.services.pandora.PandoraService",
                                                                         "programy.utils.services.google.GoogleService",
                                                                         "programy.utils.services.wikipedia.WikipediaService"])

        self.assertIn(config_data.brain_configuration.services[2].name, ["REST", "PANNOUS", "PANDORA", "WIKIPEDIA"])
        self.assertIn(config_data.brain_configuration.services[2].path, ["programy.utils.services.rest.GenericRESTService",
                                                                         "programy.utils.services.pannous.PannousService",
                                                                         "programy.utils.services.pandora.PandoraService",
                                                                         "programy.utils.services.google.GoogleService",
                                                                         "programy.utils.services.wikipedia.WikipediaService"])

        self.assertIn(config_data.brain_configuration.services[3].name, ["REST", "PANNOUS", "PANDORA", "WIKIPEDIA"])
        self.assertIn(config_data.brain_configuration.services[3].path, ["programy.utils.services.rest.GenericRESTService",
                                                                         "programy.utils.services.pannous.PannousService",
                                                                         "programy.utils.services.pandora.PandoraService",
                                                                         "programy.utils.services.google.GoogleService",
                                                                         "programy.utils.services.wikipedia.WikipediaService"])

