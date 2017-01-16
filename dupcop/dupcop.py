# -*- coding: utf-8 -*-

import logging
import hashlib
import os
import re


class DupCop(object):

    def __init__(self, logger=logging.getLogger(__name__)):
        """
        Constructor

        :param logger: Optionally provide a logger from another module if desired
        """
        self.logger = logger
        self.file_count = 0
        self.file_deleted_count = 0
        self.file_hashes = set()

    def file_hash(self, dir_file):
        """
        Returns a SHA1 hash of a file's content
        
        :param dir_file: A valid path to a file
        :return: Hash of file
        """

        try:
            with open(dir_file, 'rb') as f:
                f_hash = hashlib.sha1(f.read()).hexdigest()
                self.logger.debug('File {} has hash of {}'.format(dir_file, f_hash))
                return f_hash

        except Exception as e:
            self.logger.error('{} failed to parse with error: {}, skipping'.format(file, e))

    def delete_file(self, dir_file, dry_run=False):
        """
        Deletes a file from the operating system
        
        :param dir_file:
        :return: None
        """

        self.logger.info('Deleting file {} as a duplicate'.format(dir_file))
        self.file_deleted_count += 1

        # Do not actually delete files if the script is running in dry run mode
        if not dry_run:
            os.remove(dir_file)

    def duplicate_remove(self, dir_file, dry_run=False):
        """
        Determine if a file is a duplicate, if so delete it
        
        :param dir_file:
        :return:
        """

        self.file_count += 1
        file_hash = self.file_hash(dir_file)

        if file_hash in self.file_hashes:
            self.delete_file(dir_file, dry_run)

        else:
            self.file_hashes.add(file_hash)

    def run(self, start_path, depth_limit=None, regex_ignore=None, regex_whitelist=None, dry_run=False):
        """
        Walks a directory structure and returns a list of files
        
        :param start_path: The path in the filesystem to begin searching
        :param depth_limit:  The maximum depth to recurse
        :param regex_ignore: Ignore files matching the regex_ignore regex
        :param regex_whitelist: Only add files matching the regex_whitelist function
        :return:
        """

        if regex_ignore:
            re_ignore = re.compile(regex_ignore)

        if regex_whitelist:
            re_whitelist = re.compile(regex_whitelist)

        if depth_limit is not None:
            d_count = 0

        for dirpath, dirnames, files in os.walk(start_path):

            # Handle traversal depth
            if depth_limit:
                if d_count >= depth_limit:
                    return
                else:
                    d_count += 1

            for f in files:

                # Skip files that match an ignore regex if present
                if regex_ignore:
                    if re_ignore.match(f):
                        continue

                # If a whitelist is present, verify that files match the regex pattern
                if regex_whitelist:
                    if re_whitelist.match(f):
                        f_path = os.path.join(dirpath, f)
                        self.duplicate_remove(f_path, dry_run)

                # If a whitelist is not present process the file normally
                else:
                    f_path = os.path.join(dirpath, f)
                    self.duplicate_remove(f_path, dry_run)