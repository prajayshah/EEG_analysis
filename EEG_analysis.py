# load and plot an EEG recording file

from EEG_utils import *

a, fs, t, V = load_abf(
    initial_location='/Users/prajayshah/OneDrive - University of Toronto/UTPhD/2020/Exp 2020.1T/2020-10-19_OptoEEG')

eeg_plot(t, V, fs=fs, linewidth=0.5, ymin=-1.5, ymax=1.5, extend=10, title=a.abfFileComment,
         start=0,
         finish=600)


#%% subset of EEG data
t_sub = np.where((t > 0) & (t < 115))
V_sub = [V[0][t_sub]]

eeg_plot(t[t_sub], V_sub, fs=fs, linewidth=1.5, ymin=-1.5, ymax=1.5,
         extend=20, title=a.abfFileComment)

run_spectrum(a, fs, t, V, start=None, stop=None)
