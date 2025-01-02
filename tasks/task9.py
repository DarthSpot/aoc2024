from collections import defaultdict
from email.policy import default

from tasks.abstracttask import AbstractTask


class Task9(AbstractTask):
    def __init__(self):
        super().__init__(9)
    
    def simple_task(self):
        input = self.read_file_string()
        files = [(idx, int(l)) for idx, l in enumerate(input[::2])]
        spaces = [int(x) for x in input[1::2]]
        drive = {}
        pos = 0

        while len(files):
            head, *files = files
            idx, file_len = head
            drive[(pos, file_len)] = idx
            pos += file_len

            space, *spaces = spaces
            while space > 0 and len(files) > 0:
                filler_idx, filler_len = files[-1]
                if filler_len >= space:
                    filler_len -= space
                    drive[(pos, space)] = filler_idx
                    pos += space
                    space = 0
                else:
                    drive[(pos, filler_len)] = filler_idx
                    pos += filler_len
                    space -= filler_len
                    filler_len = 0

                if filler_len == 0:
                    files = files[:-1]
                else:
                    files[-1] = (filler_idx, filler_len)

        result = 0
        for (k_pos, k_len), idx in drive.items():
            for i in range(k_len):
                result += (k_pos + i) * idx

        return result
    
    def extended_task(self):
        input = self.read_file_string()
        files = {idx:int(l) for idx, l in enumerate(input[::2])}
        spaces = {idx:int(l) for idx, l in enumerate(input[1::2])}
        drive = []
        highest_file_idx = [x for x in files.keys()][-1]

        space_drive = defaultdict(list)
        file_it = [x for x in files.items()]
        for file_idx, file_len in file_it[::-1]:
            sp_matches = [(sp_idx, sp_len) for sp_idx, sp_len in spaces.items() if sp_len >= file_len and sp_idx < file_idx]
            if len(sp_matches) > 0:
                perf_idx, perf_len = sp_matches[0]
                spaces[perf_idx] -= file_len
                if file_idx-1 in spaces:
                    spaces[file_idx-1] += file_len
                space_drive[perf_idx].append((file_idx, file_len))
                del files[file_idx]


        for pos in range(0, highest_file_idx + 1):
            if pos in files:
                f_len = files[pos]
                drive.append((pos, f_len, False))

            for sf_idx, sf_len in space_drive[pos]:
                drive.append((sf_idx, sf_len, False))

            if pos in spaces:
                drive.append((pos, spaces[pos], True))


        result = 0
        pos = 0
        for r_idx, r_len, is_space in drive:
            if not is_space:
                for i in range(r_len):
                    result += (pos + i) * r_idx
            pos += r_len

        return result


Task9()
