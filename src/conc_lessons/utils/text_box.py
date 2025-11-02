import re
from typing import Literal

from conc_lessons.utils.ansi import Ansi

type BoxLineLargeType = tuple[str, str, str, str, str]
type BoxLineSmallType = tuple[str, str, str]

BOX_NOT_ALLOWED_RE = re.compile(r"[^a-zA-Z0-9:.~&%! ]")
NUM_CLR = Ansi.yelb + Ansi.bla
PUNC_CLR = Ansi.yelb + Ansi.bla
CHR_CLR = Ansi.blub + Ansi.whi
RES_CLR = Ansi.res

BOX_CHRS_LG: dict[str, BoxLineLargeType] = {
    "0": (
        "{num_clr} ┏━━┓ {res_clr}",
        "{num_clr} ┃  ┃ {res_clr}",
        "{num_clr} ┃  ┃ {res_clr}",
        "{num_clr} ┃  ┃ {res_clr}",
        "{num_clr} ┗━━┛ {res_clr}",
    ),
    "1": (
        "{num_clr}   ┓  {res_clr}",
        "{num_clr}   ┃  {res_clr}",
        "{num_clr}   ┃  {res_clr}",
        "{num_clr}   ┃  {res_clr}",
        "{num_clr}   ╹  {res_clr}",
    ),
    "2": (
        "{num_clr} ╺━━┓ {res_clr}",
        "{num_clr}    ┃ {res_clr}",
        "{num_clr} ┏━━┛ {res_clr}",
        "{num_clr} ┃    {res_clr}",
        "{num_clr} ┗━━╸ {res_clr}",
    ),
    "3": (
        "{num_clr} ╺━━┓ {res_clr}",
        "{num_clr}    ┃ {res_clr}",
        "{num_clr} ╺━━┫ {res_clr}",
        "{num_clr}    ┃ {res_clr}",
        "{num_clr} ╺━━┛ {res_clr}",
    ),
    "4": (
        "{num_clr} ╻  ╻ {res_clr}",
        "{num_clr} ┃  ┃ {res_clr}",
        "{num_clr} ┗━━┫ {res_clr}",
        "{num_clr}    ┃ {res_clr}",
        "{num_clr}    ╹ {res_clr}",
    ),
    "5": (
        "{num_clr} ┏━━╸ {res_clr}",
        "{num_clr} ┃    {res_clr}",
        "{num_clr} ┗━━┓ {res_clr}",
        "{num_clr}    ┃ {res_clr}",
        "{num_clr} ╺━━┛ {res_clr}",
    ),
    "6": (
        "{num_clr} ┏━━╸ {res_clr}",
        "{num_clr} ┃    {res_clr}",
        "{num_clr} ┣━━┓ {res_clr}",
        "{num_clr} ┃  ┃ {res_clr}",
        "{num_clr} ┗━━┛ {res_clr}",
    ),
    "7": (
        "{num_clr} ╺━━┓ {res_clr}",
        "{num_clr}    ┃ {res_clr}",
        "{num_clr}    ┃ {res_clr}",
        "{num_clr}    ┃ {res_clr}",
        "{num_clr}    ╹ {res_clr}",
    ),
    "8": (
        "{num_clr} ┏━━┓ {res_clr}",
        "{num_clr} ┃  ┃ {res_clr}",
        "{num_clr} ┣━━┫ {res_clr}",
        "{num_clr} ┃  ┃ {res_clr}",
        "{num_clr} ┗━━┛ {res_clr}",
    ),
    "9": (
        "{num_clr} ┏━━┓ {res_clr}",
        "{num_clr} ┃  ┃ {res_clr}",
        "{num_clr} ┗━━┫ {res_clr}",
        "{num_clr}    ┃ {res_clr}",
        "{num_clr} ╺━━┛ {res_clr}",
    ),
    "%": (  # space number
        "{num_clr}      {res_clr}",
        "{num_clr}      {res_clr}",
        "{num_clr}      {res_clr}",
        "{num_clr}      {res_clr}",
        "{num_clr}      {res_clr}",
    ),
    ":": (
        "{punc_clr}      {res_clr}",
        "{punc_clr}  ●   {res_clr}",
        "{punc_clr}      {res_clr}",
        "{punc_clr}  ●   {res_clr}",
        "{punc_clr}      {res_clr}",
    ),
    ".": (
        "{punc_clr}      {res_clr}",
        "{punc_clr}      {res_clr}",
        "{punc_clr}      {res_clr}",
        "{punc_clr}      {res_clr}",
        "{punc_clr}  ●   {res_clr}",
    ),
    "!": (  # space punctuation
        "{punc_clr}     {res_clr}",
        "{punc_clr}     {res_clr}",
        "{punc_clr}     {res_clr}",
        "{punc_clr}     {res_clr}",
        "{punc_clr}     {res_clr}",
    ),
    "a": (
        "{chr_clr} ┏━━┓ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┣━━┫ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ╹  ╹ {res_clr}",
    ),
    "b": (
        "{chr_clr} ┏━━┓ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┣━━┫ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┗━━┛ {res_clr}",
    ),
    "c": (
        "{chr_clr} ┏━━╸ {res_clr}",
        "{chr_clr} ┃    {res_clr}",
        "{chr_clr} ┃    {res_clr}",
        "{chr_clr} ┃    {res_clr}",
        "{chr_clr} ┗━━╸ {res_clr}",
    ),
    "d": (
        "{chr_clr} ┏━━┓ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┗━━┛ {res_clr}",
    ),
    "e": (
        "{chr_clr} ┏━━╸ {res_clr}",
        "{chr_clr} ┃    {res_clr}",
        "{chr_clr} ┣━━╸ {res_clr}",
        "{chr_clr} ┃    {res_clr}",
        "{chr_clr} ┗━━╸ {res_clr}",
    ),
    "f": (
        "{chr_clr} ┏━━╸ {res_clr}",
        "{chr_clr} ┃    {res_clr}",
        "{chr_clr} ┣━━╸ {res_clr}",
        "{chr_clr} ┃    {res_clr}",
        "{chr_clr} ╹    {res_clr}",
    ),
    "g": (
        "{chr_clr} ┏━━╸ {res_clr}",
        "{chr_clr} ┃    {res_clr}",
        "{chr_clr} ┃ ━┓ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┗━━┛ {res_clr}",
    ),
    "h": (
        "{chr_clr} ╻  ╻ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┣━━┫ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ╹  ╹ {res_clr}",
    ),
    "i": (
        "{chr_clr}   ╻  {res_clr}",
        "{chr_clr}   ╻  {res_clr}",
        "{chr_clr}   ┃  {res_clr}",
        "{chr_clr}   ┃  {res_clr}",
        "{chr_clr}   ╹  {res_clr}",
    ),
    "j": (
        "{chr_clr}   ━┓ {res_clr}",
        "{chr_clr}    ┃ {res_clr}",
        "{chr_clr}    ┃ {res_clr}",
        "{chr_clr}    ┃ {res_clr}",
        "{chr_clr} ┗━━┛ {res_clr}",
    ),
    "k": (
        "{chr_clr} ╻┏╸  {res_clr}",
        "{chr_clr} ┃┃   {res_clr}",
        "{chr_clr} ┣┻┓  {res_clr}",
        "{chr_clr} ┃ ┃  {res_clr}",
        "{chr_clr} ╹ ┗╸ {res_clr}",
    ),
    "l": (
        "{chr_clr} ╻    {res_clr}",
        "{chr_clr} ┃    {res_clr}",
        "{chr_clr} ┃    {res_clr}",
        "{chr_clr} ┃    {res_clr}",
        "{chr_clr} ┗━━╸ {res_clr}",
    ),
    "m": (
        "{chr_clr} ┏━┳┓ {res_clr}",
        "{chr_clr} ┃ ┃┃ {res_clr}",
        "{chr_clr} ┃ ┃┃ {res_clr}",
        "{chr_clr} ┃ ┃┃ {res_clr}",
        "{chr_clr} ╹ ╹╹ {res_clr}",
    ),
    "n": (
        "{chr_clr} ┳━━┓ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ╹  ╹ {res_clr}",
    ),
    "o": (
        "{chr_clr} ┏━━┓ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┗━━┛ {res_clr}",
    ),
    "p": (
        "{chr_clr} ┏━━┓ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┣━━┛ {res_clr}",
        "{chr_clr} ┃    {res_clr}",
        "{chr_clr} ╹    {res_clr}",
    ),
    "q": (
        "{chr_clr} ┏━━┓ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┗━┻╋ {res_clr}",
    ),
    "r": (
        "{chr_clr} ┏━━┓ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┣━┳┛ {res_clr}",
        "{chr_clr} ┃ ┃  {res_clr}",
        "{chr_clr} ╹ ╹  {res_clr}",
    ),
    "s": (
        "{chr_clr} ┏━━╸ {res_clr}",
        "{chr_clr} ┃    {res_clr}",
        "{chr_clr} ┗━━┓ {res_clr}",
        "{chr_clr}    ┃ {res_clr}",
        "{chr_clr} ╺━━┛ {res_clr}",
    ),
    "t": (
        "{chr_clr} ╺━┳━ {res_clr}",
        "{chr_clr}   ┃  {res_clr}",
        "{chr_clr}   ┃  {res_clr}",
        "{chr_clr}   ┃  {res_clr}",
        "{chr_clr}   ╹  {res_clr}",
    ),
    "u": (
        "{chr_clr} ╻  ╻ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┗━━┛ {res_clr}",
    ),
    "v": (
        "{chr_clr} ╻  ╻ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┃ ┏┛ {res_clr}",
        "{chr_clr} ┗━┛  {res_clr}",
    ),
    "w": (
        "{chr_clr} ╻  ╻ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┃ ┃┃ {res_clr}",
        "{chr_clr} ┃ ┃┃ {res_clr}",
        "{chr_clr} ┗━┻┛ {res_clr}",
    ),
    "x": (
        "{chr_clr} ╺┓┏╸ {res_clr}",
        "{chr_clr}  ┃┃  {res_clr}",
        "{chr_clr} ┏┗┓  {res_clr}",
        "{chr_clr} ┃ ┃  {res_clr}",
        "{chr_clr} ┛ ┗╸ {res_clr}",
    ),
    "y": (
        "{chr_clr} ╻  ╻ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┗━┳┛ {res_clr}",
        "{chr_clr}   ┃  {res_clr}",
        "{chr_clr}   ╹  {res_clr}",
    ),
    "z": (
        "{chr_clr} ╺━━┓ {res_clr}",
        "{chr_clr}    ┃ {res_clr}",
        "{chr_clr} ┏━━┛ {res_clr}",
        "{chr_clr} ┃    {res_clr}",
        "{chr_clr} ┗━━╸ {res_clr}",
    ),
    "&": (  # space char
        "{chr_clr}      {res_clr}",
        "{chr_clr}      {res_clr}",
        "{chr_clr}      {res_clr}",
        "{chr_clr}      {res_clr}",
        "{chr_clr}      {res_clr}",
    ),
    "~": (  # space no color
        "{res_clr}      {res_clr}",
        "{res_clr}      {res_clr}",
        "{res_clr}      {res_clr}",
        "{res_clr}      {res_clr}",
        "{res_clr}      {res_clr}",
    ),
}

BOX_CHRS_SM: dict[str, BoxLineSmallType] = {
    "0": (
        "{num_clr} ┏━━┓ {res_clr}",
        "{num_clr} ┃  ┃ {res_clr}",
        "{num_clr} ┗━━┛ {res_clr}",
    ),
    "1": (
        "{num_clr}   ┓  {res_clr}",
        "{num_clr}   ┃  {res_clr}",
        "{num_clr}   ╹  {res_clr}",
    ),
    "2": (
        "{num_clr} ╺━━┓ {res_clr}",
        "{num_clr} ┏━━┛ {res_clr}",
        "{num_clr} ┗━━╸ {res_clr}",
    ),
    "3": (
        "{num_clr} ╺━━┓ {res_clr}",
        "{num_clr} ╺━━┫ {res_clr}",
        "{num_clr} ╺━━┛ {res_clr}",
    ),
    "4": (
        "{num_clr} ╻  ╻ {res_clr}",
        "{num_clr} ┗━━┫ {res_clr}",
        "{num_clr}    ╹ {res_clr}",
    ),
    "5": (
        "{num_clr} ┏━━╸ {res_clr}",
        "{num_clr} ┗━━┓ {res_clr}",
        "{num_clr} ╺━━┛ {res_clr}",
    ),
    "6": (
        "{num_clr} ┏━━╸ {res_clr}",
        "{num_clr} ┣━━┓ {res_clr}",
        "{num_clr} ┗━━┛ {res_clr}",
    ),
    "7": (
        "{num_clr} ╺━━┓ {res_clr}",
        "{num_clr}    ┃ {res_clr}",
        "{num_clr}    ╹ {res_clr}",
    ),
    "8": (
        "{num_clr} ┏━━┓ {res_clr}",
        "{num_clr} ┣━━┫ {res_clr}",
        "{num_clr} ┗━━┛ {res_clr}",
    ),
    "9": (
        "{num_clr} ┏━━┓ {res_clr}",
        "{num_clr} ┗━━┫ {res_clr}",
        "{num_clr} ╺━━┛ {res_clr}",
    ),
    "%": (  # space number
        "{num_clr}      {res_clr}",
        "{num_clr}      {res_clr}",
        "{num_clr}      {res_clr}",
    ),
    ":": (
        "{punc_clr}      {res_clr}",
        "{punc_clr}  ▪   {res_clr}",
        "{punc_clr}  ▪   {res_clr}",
    ),
    ".": (
        "{punc_clr}      {res_clr}",
        "{punc_clr}      {res_clr}",
        "{punc_clr}  ▪   {res_clr}",
    ),
    "!": (  # space punctuation
        "{punc_clr}     {res_clr}",
        "{punc_clr}     {res_clr}",
        "{punc_clr}     {res_clr}",
    ),
    "a": (
        "{chr_clr} ┏━━┓ {res_clr}",
        "{chr_clr} ┣━━┫ {res_clr}",
        "{chr_clr} ╹  ╹ {res_clr}",
    ),
    "b": (
        "{chr_clr} ┏━━┓ {res_clr}",
        "{chr_clr} ┣━━┫ {res_clr}",
        "{chr_clr} ┗━━┛ {res_clr}",
    ),
    "c": (
        "{chr_clr} ┏━━╸ {res_clr}",
        "{chr_clr} ┃    {res_clr}",
        "{chr_clr} ┗━━╸ {res_clr}",
    ),
    "d": (
        "{chr_clr} ┏━━┓ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┗━━┛ {res_clr}",
    ),
    "e": (
        "{chr_clr} ┏━━╸ {res_clr}",
        "{chr_clr} ┣━━╸ {res_clr}",
        "{chr_clr} ┗━━╸ {res_clr}",
    ),
    "f": (
        "{chr_clr} ┏━━╸ {res_clr}",
        "{chr_clr} ┣━━╸ {res_clr}",
        "{chr_clr} ╹    {res_clr}",
    ),
    "g": (
        "{chr_clr} ┏━━╸ {res_clr}",
        "{chr_clr} ┃ ━┓ {res_clr}",
        "{chr_clr} ┗━━┛ {res_clr}",
    ),
    "h": (
        "{chr_clr} ╻  ╻ {res_clr}",
        "{chr_clr} ┣━━┫ {res_clr}",
        "{chr_clr} ╹  ╹ {res_clr}",
    ),
    "i": (
        "{chr_clr}   ╻  {res_clr}",
        "{chr_clr}   ┃  {res_clr}",
        "{chr_clr}   ╹  {res_clr}",
    ),
    "j": (
        "{chr_clr}   ━┓ {res_clr}",
        "{chr_clr}    ┃ {res_clr}",
        "{chr_clr} ┗━━┛ {res_clr}",
    ),
    "k": (
        "{chr_clr} ╻┏╸  {res_clr}",
        "{chr_clr} ┣┻┓  {res_clr}",
        "{chr_clr} ╹ ┗╸ {res_clr}",
    ),
    "l": (
        "{chr_clr} ╻    {res_clr}",
        "{chr_clr} ┃    {res_clr}",
        "{chr_clr} ┗━━╸ {res_clr}",
    ),
    "m": (
        "{chr_clr} ┏━┳┓ {res_clr}",
        "{chr_clr} ┃ ┃┃ {res_clr}",
        "{chr_clr} ╹ ╹╹ {res_clr}",
    ),
    "n": (
        "{chr_clr} ┳━━┓ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ╹  ╹ {res_clr}",
    ),
    "o": (
        "{chr_clr} ┏━━┓ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┗━━┛ {res_clr}",
    ),
    "p": (
        "{chr_clr} ┏━━┓ {res_clr}",
        "{chr_clr} ┣━━┛ {res_clr}",
        "{chr_clr} ╹    {res_clr}",
    ),
    "q": (
        "{chr_clr} ┏━━┓ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┗━┻╋ {res_clr}",
    ),
    "r": (
        "{chr_clr} ┏━━┓ {res_clr}",
        "{chr_clr} ┣━┳┛ {res_clr}",
        "{chr_clr} ╹ ╹  {res_clr}",
    ),
    "s": (
        "{chr_clr} ┏━━╸ {res_clr}",
        "{chr_clr} ┗━━┓ {res_clr}",
        "{chr_clr} ╺━━┛ {res_clr}",
    ),
    "t": (
        "{chr_clr} ╺━┳━ {res_clr}",
        "{chr_clr}   ┃  {res_clr}",
        "{chr_clr}   ╹  {res_clr}",
    ),
    "u": (
        "{chr_clr} ╻  ╻ {res_clr}",
        "{chr_clr} ┃  ┃ {res_clr}",
        "{chr_clr} ┗━━┛ {res_clr}",
    ),
    "v": (
        "{chr_clr} ╻  ╻ {res_clr}",
        "{chr_clr} ┃ ┏┛ {res_clr}",
        "{chr_clr} ┗━┛  {res_clr}",
    ),
    "w": (
        "{chr_clr} ╻  ╻ {res_clr}",
        "{chr_clr} ┃ ┃┃ {res_clr}",
        "{chr_clr} ┗━┻┛ {res_clr}",
    ),
    "x": (
        "{chr_clr} ╺┓┏╸ {res_clr}",
        "{chr_clr} ┏┗┓  {res_clr}",
        "{chr_clr} ┛ ┗╸ {res_clr}",
    ),
    "y": (
        "{chr_clr} ╻  ╻ {res_clr}",
        "{chr_clr} ┗━┳┛ {res_clr}",
        "{chr_clr}   ╹  {res_clr}",
    ),
    "z": (
        "{chr_clr} ╺━━┓ {res_clr}",
        "{chr_clr} ┏━━┛ {res_clr}",
        "{chr_clr} ┗━━╸ {res_clr}",
    ),
    "&": (  # space char
        "{chr_clr}      {res_clr}",
        "{chr_clr}      {res_clr}",
        "{chr_clr}      {res_clr}",
    ),
    "~": (  # space no color
        "{res_clr}      {res_clr}",
        "{res_clr}      {res_clr}",
        "{res_clr}      {res_clr}",
    ),
}


def compose_box_chrs(
    text: str,
    num_clr: str = "",
    chr_clr: str = "",
    punc_clr: str = "",
    res_clr: str = "",
    size: Literal["LG", "SM"] = "SM",
) -> str:
    cleaned_text = BOX_NOT_ALLOWED_RE.sub("", text.strip())
    text_words = cleaned_text.split(" ")
    final_text = ""
    box_chrs = BOX_CHRS_SM if size == "SM" else BOX_CHRS_LG

    for word in text_words:
        box_lines = [box_chrs[character.lower()] for character in word]

        for box_line in zip(*box_lines, strict=False):
            # line by line here
            # final_text += Ansi.rand_bg()  # BG line by line
            # final_text += Ansi.rand_fg()  # FG line by line
            for str_line in box_line:
                # words by word here
                # final_text += Ansi.rand_bg()  # BG word by word
                # final_text += Ansi.rand_fg()  # FG word by word
                for char in str_line.format(
                    num_clr=num_clr,
                    chr_clr=chr_clr,
                    punc_clr=punc_clr,
                    res_clr=res_clr,
                ):
                    # char by char here
                    # final_text += Ansi.rand_bg()  # BG char by char
                    # final_text += Ansi.rand_fg()  # FG char by char
                    final_text += char

                    # final_text += Ansi.res  # reset char by char
                # final_text += Ansi.res # reset word by word
            # final_text += Ansi.res # reset line by line
            final_text += "\n"

    return final_text


if __name__ == "__main__":
    number_with_letter = compose_box_chrs(
        "100k",
        res_clr=Ansi.res,
        chr_clr=f"{Ansi.purb}{Ansi.bla}",
        punc_clr=f"{Ansi.purb}{Ansi.bla}",
        num_clr=f"{Ansi.pinb}{Ansi.bla}",
    )
    clock = compose_box_chrs(
        "14:22:11",
        res_clr=Ansi.res,
        chr_clr=f"{Ansi.gre}",
        punc_clr=f"{Ansi.yel}",
        num_clr=f"{Ansi.gre}",
    )
    python_logo = compose_box_chrs(
        "&Python&%3.14%",
        res_clr=Ansi.res,
        chr_clr=f"{Ansi.blub}{Ansi.whi}",
        punc_clr=f"{Ansi.yelb}{Ansi.bla}",
        num_clr=f"{Ansi.yelb}{Ansi.bla}",
    )

    print(number_with_letter)
    print(clock)
    print(python_logo)
