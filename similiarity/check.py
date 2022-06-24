import glob
import os

import pandas as pd
from similiarity.export.template.build import clean_path_
from similiarity.export.to_html import c_html

from similiarity.products import *
from similiarity.freq_mapping import *

class CheckSimiliar:
    _files_ = []
    __results_ = []
    __bulk_results_ = []


    def __init__(self, path_files, extension, tolerance=70):
        self.__path_files = self._clean_path_(path_files)
        self._tolerance = tolerance

        for file in glob.glob(path_files + '/*' + extension):
            self._files_.append(file)

        self._checkSimiliarity_()

        self._bulk_results_()

    
    def _checkSimiliarity_(self):

        for source in range(len(self._files_)):
            file_source = self._files_[source]

            words, chars, sorted_word_file_source = word_frequencies_for_file(file_source)

            temp_file_checked = []
            for file_check in self._files_:
                if file_source == file_check:
                    continue
                else:
                    sorted_word_file_check = word_frequencies_for_file(file_check)[-1]

                    distance_score = vector_angle(sorted_word_file_source, sorted_word_file_check)
                    distance_score = round(distance_score, 4)

                    # Ubah nilai range score menjadi range persen
                    # 100% --> 1.5708
                    # ((score - min_persen) / (maks_score - min_score)) * (maks_persen - min_persen)
                    distance_score = ( ( distance_score - 0.0 ) / (1.5708 - 0.0) ) * (100 - 0)
                    distance_score = 100 - distance_score

                    temp_file_checked.append([file_check, distance_score])
                
            self.__results_.append([file_source, temp_file_checked, words, chars])

    def _bulk_results_(self):
        results = self.__results_
        bulk_results = []

        for result in results:
            file_source = result[0]

            for res in result[1]:
                file_source = self._remove_path_file(file_source)
                file_check = self._remove_path_file(res[0])

                score = res[-1]

                conclusion = self._conclusion_(score)

                bulk_results.append( [file_source, file_check, score, conclusion] )
        
        self.__bulk_results_ = bulk_results


    def _remove_path_file(self, file):
        return file.replace(self.__path_files + "\\", '')


    def _conclusion_(self, score):
        if score > self._tolerance:
            return "PLAGIARISM DETECTED !!!"
        else:
            return "UNIQUE"

    def _clean_path_(self, path):
        return clean_path_(path)

    def results_(self):
        return self.__results_

    def bulk_results_(self):
        return self.__bulk_results_

    def files_(self):
        files = []

        for temp_file in self._files_:
            files.append(self._remove_path_file(temp_file))
        
        return files

    def export(self):
        
        for file in glob.glob("export/*.html"):
            os.remove(file)

        c_html(self.results_(), self._tolerance)