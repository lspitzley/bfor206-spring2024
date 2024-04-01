"""
Tests for the youtube_metadata_download.py script.
"""

#%% imports

import unittest

# import the downloader script
import youtube_metadata_download as ymd

#%% create test class

class TestVideoDownloader(unittest.TestCase):
    
    def test_ceo_in_title(self):    
        """
        Test that the get_channel_videos function returns a list of video links.
        """
        test_title = "Redfin CEO reacts to NAR's $418 million commission lawsuits settlement"
        # test the function
        has_ceo = ymd.ceo_in_title(test_title)
        # check the result
        self.assertTrue(has_ceo)

        test_title = "TikTok is a national security risk that needs to be banned, says Slow Ventures' Sam Lessin"
        has_ceo = ymd.ceo_in_title(test_title)
        self.assertFalse(has_ceo)

    def test_clean_view_count(self):
        # define test cases here
        pass


    def test_get_video_duration(self):
        """
        This function tests the get_video_duration function. The function
        takes strings of video duration and returns the duration in seconds.
        """
        
        test_data_1 = "01:30"
        test_data_2 = "01:30:45"

        result_1 = ymd.get_video_duration(test_data_1)
        self.assertEqual(result_1, 90)

        result_2 = ymd.get_video_duration(test_data_2)
        self.assertEqual(result_2, 5445)

if __name__ == '__main__':
    unittest.main()