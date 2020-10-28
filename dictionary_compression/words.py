# dictionary compression library by spiritplumber@gmail.com
# should be useful for the purpose of compressing text messages and so on
# scramble word list for (crappy) encryption
# CC attribution noncommercial sharealike 2020

wordlist=[
'ability',
'able',
'about',
'above',
'abroad',
'absolute',
'abuse',
'accept',
'access',
'accident',
'accord',
'account',
'accurate',
'accus',
'achieve',
'acid',
'acquire',
'across',
'act',
'activ',
'actor',
'actual',
'ad',
'adapt',
'add',
'addition',
'additional',
'address',
'adjust',
'administrat',
'admir',
'admit',
'adopt',
'adult',
'advance',
'advanced',
'advantage',
'advertis',
'advice',
'affair',
'affect',
'afford',
'afraid',
'after',
'afternoon',
'again',
'against',
'age',
'agency',
'agent',
'aggress',
'agil',
'ago',
'agree',
'ahead',
'air',
'airline',
'airport',
'alarm',
'alcohol',
'al',
'all',
'allow',
'almost',
'alone',
'along',
'already',
'also',
'alternat',
'although',
'altogether',
'always',
'am',
'amaz',
'ambition',
'americ',
'among',
'amount',
'an',
'analysis',
'analyst',
'and',
'anger',
'angle',
'angry',
'animal',
'announce',
'annual',
'another',
'answer',
'anticipate',
'anxiety',
'anxious',
'any',
'anybody',
'anyone',
'anyth',
'anyway',
'anywhere',
'apart',
'apologiz',
'app',
'appeal',
'appear',
'appearance',
'apple',
'applic',
'appoint',
'appreciat',
'approach',
'appropriat',
'approve',
'are',
'area',
'argu',
'argue',
'aris',
'arm',
'army',
'around',
'arrival',
'arriv',
'art',
'article',
'as',
'aside',
'ask',
'asleep',
'aspect',
'assassin',
'assign',
'assist',
'assistance',
'assistant',
'associ',
'assume',
'assumption',
'ass',
'at',
'atmosphere',
'attach',
'attack',
'attempt',
'attend',
'attention',
'attitude',
'attract',
'audience',
'author',
'automatic',
'avail',
'average',
'avoid',
'award',
'aware',
'awareness',
'away',
'awesome',
'baby',
'back',
'background',
'bad',
'bag',
'bake',
'balance',
'ball',
'band',
'bank',
'bar',
'base',
'baseball',
'basic',
'basical',
'basis',
'basket',
'bat',
'bath',
'bathroom',
'battle',
'be',
'beach',
'bear',
'beat',
'beautiful',
'because',
'become',
'bed',
'bedroom',
'been',
'beer',
'before',
'begin',
'beginn',
'behave',
'behind',
'believ',
'bell',
'belong',
'below',
'belt',
'bench',
'bend',
'benefit',
'best',
'bet',
'better',
'between',
'beyond',
'bicycle',
'bid',
'big',
'bike',
'bil',
'bill',
'bird',
'birth',
'birthday',
'bit',
'bitch',
'bite',
'bitter',
'black',
'blame',
'blank',
'blind',
'block',
'blood',
'blow',
'blue',
'board',
'boat',
'body',
'bone',
'bonus',
'boobies',
'book',
'boot',
'bor',
'border',
'born',
'borrow',
'boss',
'both',
'bother',
'bottle',
'bottom',
'bowl',
'box',
'boy',
'boyfriend',
'br',
'brain',
'branch',
'brave',
'bread',
'break',
'breakfast',
'breast',
'breasts',
'breath',
'brick',
'bridge',
'brief',
'bright',
'brilliant',
'broad',
'brother',
'brown',
'brush',
'buddy',
'budget',
'bug',
'build',
'bunch',
'burn',
'bus',
'business',
'busy',
'but',
'button',
'buy',
'buyer',
'by',
'cabinet',
'cake',
'calculat',
'calendar',
'call',
'calm',
'came',
'camera',
'camp',
'campaign',
'can',
'cancel',
'cancer',
'candid',
'candle',
'candy',
'cap',
'capital',
'car',
'card',
'care',
'career',
'careful',
'carpet',
'carry',
'case',
'cash',
'cat',
'catch',
'category',
'caus',
'celebrat',
'cell',
'certain',
'chain',
'chair',
'challenge',
'champ',
'championship',
'chance',
'change',
'channel',
'chapter',
'character',
'charge',
'charity',
'chart',
'cheap',
'check',
'cheek',
'chemical',
'chemistry',
'chest',
'chicken',
'child',
'childhood',
'chip',
'chocolate',
'choice',
'choos',
'church',
'cigarette',
'city',
'civil',
'claim',
'class',
'classic',
'classroom',
'clean',
'clear',
'clerk',
'click',
'client',
'climate',
'clock',
'clos',
'closed',
'closet',
'clothes',
'cloud',
'club',
'clue',
'coach',
'coast',
'coat',
'cod',
'coffee',
'cold',
'collar',
'collect',
'college',
'com',
'combin',
'come',
'comfort',
'command',
'commercial',
'commission',
'commit',
'committee',
'common',
'commun',
'communic',
'company',
'compare',
'comparison',
'compete',
'competit',
'complain',
'complaint',
'complete',
'complex',
'complicat',
'comprehens',
'compress',
'computer',
'concentrate',
'concept',
'concern',
'concerned',
'concert',
'conclusion',
'condition',
'conference',
'confidence',
'confident',
'confirm',
'conflict',
'confus',
'connect',
'conscious',
'consequence',
'conservat',
'consider',
'consist',
'consistent',
'constant',
'construct',
'consult',
'contact',
'contain',
'content',
'contest',
'context',
'continue',
'contract',
'contribut',
'control',
'convers',
'convert',
'convince',
'cook',
'cookie',
'cookies',
'cool',
'copy',
'corner',
'correct',
'cost',
'could',
'count',
'counter',
'countries',
'country',
'county',
'couple',
'courage',
'course',
'court',
'cousin',
'cover',
'cow',
'crack',
'craft',
'crash',
'crazy',
'cream',
'creat',
'credit',
'crew',
'critic',
'critical',
'criticiz',
'cross',
'cry',
'cultural',
'cult',
'cup',
'curious',
'currency',
'current',
'curve',
'customer',
'cut',
'cute',
'cycle',
'dad',
'dai',
'damage',
'dance',
'danger',
'dangerous',
'dare',
'dark',
'data',
'database',
'date',
'daughter',
'day',
'dead',
'deal',
'dealer',
'dear',
'death',
'debate',
'debt',
'decent',
'decide',
'decision',
'deep',
'definit',
'degree',
'delay',
'deliberat',
'deliver',
'delivery',
'delus',
'demand',
'depart',
'depend',
'dependent',
'depict',
'deposit',
'depress',
'depth',
'derp',
'describe',
'description',
'deserv',
'design',
'designer',
'desire',
'desk',
'desperat',
'despite',
'destroy',
'detail',
'determin',
'develop',
'device',
'devil',
'diamond',
'dick',
'die',
'diet',
'differ',
'difference',
'different',
'difficult',
'difficulty',
'dig',
'dimension',
'dinner',
'direct',
'director',
'dirt',
'dirty',
'disagree',
'disappoint',
'disaster',
'disciplin',
'discount',
'discover',
'discuss',
'disease',
'dish',
'disk',
'display',
'distance',
'distinct',
'distribut',
'district',
'divide',
'do',
'doctor',
'document',
'does',
'dog',
'door',
'dot',
'double',
'doubt',
'down',
'downtown',
'draft',
'drag',
'drama',
'dramatic',
'draw',
'drawer',
'dream',
'dress',
'drink',
'drive',
'driver',
'drop',
'drunk',
'dry',
'due',
'dump',
'dur',
'dust',
'duty',
'each',
'ear',
'earn',
'earth',
'ease',
'easier',
'east',
'eastern',
'easy',
'eat',
'economics',
'economy',
'edge',
'editor',
'educat',
'effect',
'efficiency',
'efficient',
'effort',
'egg',
'either',
'election',
'electrical',
'electronic',
'elevator',
'else',
'elsewhere',
'embarrass',
'emergency',
'emotion',
'emotional',
'emphasis',
'emphasize',
'employ',
'employe',
'employer',
'empty',
'en',
'encourag',
'end',
'energy',
'engage',
'engine',
'engineer',
'enhance',
'enjoy',
'enough',
'ensure',
'enter',
'entertain',
'enthusiasm',
'entire',
'entrance',
'entry',
'environ',
'environmental',
'equal',
'equip',
'equivalent',
'error',
'escape',
'essay',
'essential',
'establish',
'estate',
'estimate',
'even',
'event',
'eventual',
'ever',
'every',
'everybody',
'everyone',
'everyth',
'everywhere',
'evidence',
'exact',
'exam',
'examination',
'examine',
'example',
'excellent',
'except',
'exchange',
'excit',
'excite',
'excuse',
'exercise',
'exist',
'exit',
'expand',
'expans',
'expect',
'expens',
'experienc',
'expert',
'explain',
'explanation',
'explor',
'expos',
'express',
'extend',
'extension',
'extent',
'external',
'extra',
'extreme',
'eye',
'face',
'fact',
'factor',
'fail',
'fair',
'fall',
'false',
'fami',
'familiar',
'famous',
'fan',
'fantastic',
'far',
'farm',
'farmer',
'fast',
'fat',
'father',
'fault',
'fear',
'feat',
'federal',
'fee',
'feed',
'feedback',
'feel',
'female',
'few',
'field',
'fight',
'fig',
'file',
'fill',
'film',
'final',
'finance',
'financial',
'find',
'fine',
'finger',
'finish',
'fire',
'firm',
'first',
'fish',
'fit',
'fix',
'fixed',
'flat',
'flight',
'floor',
'flow',
'flower',
'focus',
'fold',
'follow',
'food',
'foot',
'football',
'for',
'force',
'foreign',
'forever',
'forget',
'form',
'formal',
'former',
'forth',
'fortune',
'forward',
'found',
'frame',
'free',
'freedom',
'frequent',
'fresh',
'friend',
'friendship',
'from',
'front',
'fruit',
'fuck',
'fuel',
'ful',
'full',
'fun',
'function',
'funeral',
'funny',
'fut',
'gain',
'game',
'gap',
'garage',
'garbage',
'garden',
'gas',
'gate',
'gather',
'gear',
'gene',
'general',
'generat',
'gent',
'get',
'gift',
'girl',
'girlfriend',
'give',
'glad',
'glass',
'global',
'glove',
'go',
'goal',
'god',
'gold',
'golf',
'gonna',
'good',
'govern',
'grab',
'grad',
'grand',
'grandfather',
'grandmother',
'graphic',
'grass',
'great',
'green',
'grocery',
'gross',
'ground',
'group',
'grow',
'growth',
'guarantee',
'guard',
'guess',
'guest',
'guid',
'guidance',
'guidelin',
'guilty',
'guitar',
'guy',
'habit',
'had',
'hair',
'half',
'hall',
'hand',
'handl',
'hang',
'happen',
'happy',
'hard',
'harm',
'has',
'hat',
'hate',
'have',
'he',
'head',
'health',
'healthy',
'hear',
'heart',
'heat',
'heavy',
'height',
'hell',
'hello',
'help',
'helpful',
'her',
'here',
'herself',
'hesitate',
'hi',
'hide',
'high',
'highlight',
'highway',
'him',
'himself',
'hire',
'his',
'historian',
'historical',
'history',
'hit',
'hold',
'hole',
'holiday',
'home',
'homework',
'honest',
'honey',
'hook',
'hope',
'hopeful',
'horror',
'horse',
'hospital',
'host',
'hot',
'hotel',
'hour',
'hous',
'house',
'how',
'however',
'huge',
'human',
'hungry',
'hunt',
'hurry',
'hurt',
'husband', "i'm", 'ice',
'idea',
'ideal',
'identify',
'if',
'ignor',
'ill',
'illegal',
'illustrat',
'image',
'imagin',
'imagine',
'immediate',
'imp',
'impact',
'imple',
'importance',
'important',
'impos',
'impossible',
'impress',
'improve',
'in',
'incident',
'includ',
'include',
'income',
'incorporat',
'increase',
'independence',
'independent',
'indic',
'indicat',
'individual',
'industry',
'inevit',
'influence',
'inform',
'informal',
'initial',
'initiat',
'injury',
'inner',
'insect',
'inside',
'insist',
'inspect',
'inspector',
'install',
'instance',
'instead',
'instruct',
'insurance',
'intelligent',
'intend',
'intent',
'interaction',
'interest',
'intern',
'international',
'internet',
'interview',
'into',
'introduce',
'introduct',
'invest',
'investigat',
'invit',
'involve',
'involved',
'iron',
'is',
'island',
'issu',
'it',
'it\'s',
'item',
'its',
'itself',
'jacket',
'job',
'join',
'joint',
'joke',
'judg',
'judge',
'juice',
'jump',
'junior',
'jury',
'just',
'justify',
'keep',
'key',
'kick',
'kid',
'kill',
'kind',
'kiss',
'kitchen',
'kitty',
'knee',
'knife',
'know',
'knowledge',
'known',
'lab',
'lack',
'ladder',
'lady',
'lake',
'land',
'landscape',
'language',
'large',
'last',
'late',
'later',
'latter',
'laugh',
'law',
'lawyer',
'lay',
'layer',
'lead',
'leader',
'leadership',
'league',
'learn',
'least',
'leather',
'leave',
'lect',
'left',
'leg',
'legal',
'length',
'less',
'lesson',
'let',
'let\'s',
'letter',
'level',
'liberty',
'library',
'lie',
'life',
'lift',
'light',
'like',
'limit',
'limited',
'line',
'link',
'lip',
'list',
'listen',
'literal',
'literat',
'little',
'liv',
'load',
'loan',
'local',
'locat',
'lock',
'log',
'logical',
'lone',
'long',
'look',
'loose',
'lose',
'loss',
'lost',
'lot',
'loud',
'lov',
'low',
'lower',
'luck',
'lucky',
'lunch',
'machine',
'mad',
'magazine',
'mail',
'main',
'maintain',
'maintenance',
'major',
'make',
'male',
'mall',
'man',
'manage',
'manager',
'manner',
'manufactur',
'manufacturer',
'many',
'map',
'march',
'mark',
'market',
'marriage',
'married',
'marry',
'mass',
'master',
'match',
'mate',
'material',
'math',
'matter',
'max',
'maximum',
'may',
'maybe',
'me',
'meal',
'mean',
'measure',
'meat',
'media',
'medic',
'medicine',
'medium',
'meet',
'member',
'membership',
'memory',
'ment',
'menu',
'mere',
'mess',
'message',
'messages',
'metal',
'method',
'middle',
'midnight',
'might',
'milk',
'mind',
'mine',
'mini',
'minimum',
'minister',
'ministry',
'minor',
'minute',
'mirror',
'miss',
'mistake',
'mix',
'mixed',
'mixture',
'mo',
'mobile',
'mode',
'model',
'mom',
'money',
'monitor',
'month',
'mood',
'more',
'moreover',
'morn',
'mortgage',
'most',
'mother',
'motor',
'mountain',
'mouse',
'mouth',
'move',
'movie',
'movies',
'much',
'mud',
'muscle',
'music',
'must',
'my',
'myself',
'nail',
'name',
'narrow',
'nasty',
'nation',
'natural',
'nat',
'near',
'nearby',
'neat',
'necessari',
'necessary',
'neck',
'need',
'negativ',
'negotiat',
'negotiation',
'neither',
'nerve',
'nervous',
'net',
'network',
'never',
'new',
'news',
'newspaper',
'next',
'nice',
'night',
'no',
'nobody',
'noise',
'none',
'nor',
'normal',
'north',
'nose',
'not',
'note',
'noth',
'notice',
'novel',
'now',
'nowhere',
'number',
'numerous',
'nurse',
'object',
'oblig',
'obtain',
'obvious',
'occasion',
'occasional',
'occur',
'odd',
'of',
'off',
'offer',
'office',
'officer',
'official',
'often',
'oil',
'ok',
'old',
'on',
'once',
'one',
'online',
'open',
'oper',
'operat',
'opin',
'opportun',
'opposite',
'opt',
'or',
'orange',
'order',
'ordinary',
'organiz',
'original',
'other',
'otherwise',
'ought',
'our',
'ourselves',
'out',
'outcome',
'outside',
'oven',
'over',
'overall',
'overcome',
'owe',
'own',
'owner',
'pace',
'pack',
'package',
'page',
'pain',
'paint',
'pair',
'pandemic',
'panic',
'paper',
'parent',
'park',
'part',
'participat',
'particular',
'partner',
'party',
'pass',
'passage',
'passenger',
'passion',
'past',
'path',
'patience',
'patient',
'pattern',
'pause',
'pay',
'peace',
'peak',
'pen',
'penalty',
'penis',
'pension',
'people',
'percentage',
'perception',
'perfect',
'perform',
'performance',
'period',
'permission',
'permit',
'person',
'personal',
'perspective',
'persuade',
'phase',
'philosophy',
'phone',
'photo',
'phras',
'physical',
'physics',
'piano',
'pick',
'pict',
'pie',
'piece',
'pin',
'pipe',
'pitch',
'pizza',
'place',
'plan',
'plane',
'plant',
'plastic',
'plate',
'platform',
'play',
'player',
'pleas',
'pleasant',
'plenty',
'plural',
'plus',
'poem',
'poet',
'poetry',
'point',
'police',
'policy',
'political',
'politics',
'pollution',
'pool',
'poor',
'pop',
'popul',
'popular',
'position',
'positiv',
'possess',
'possibility',
'possibl',
'post',
'pot',
'potato',
'potential',
'pound',
'pour',
'power',
'powerful',
'practical',
'practice',
'pray',
'prefer',
'preference',
'pregnant',
'prepar',
'presence',
'present',
'president',
'press',
'pretend',
'pretty',
'prevent',
'previous',
'price',
'pride',
'priest',
'primary',
'principal',
'principle',
'print',
'prior',
'priv',
'prize',
'probab',
'problem',
'procedure',
'process',
'produce',
'product',
'profess',
'professor',
'profil',
'profit',
'program',
'progress',
'project',
'promise',
'promot',
'prompt',
'proof',
'proper',
'property',
'propos',
'proposal',
'protect',
'proud',
'prove',
'provid',
'psychological',
'psychology',
'public',
'pull',
'punch',
'purchase',
'pure',
'purple',
'purpose',
'pursue',
'push',
'pussy',
'put',
'qual',
'qualify',
'quant',
'quarter',
'queen',
'quest',
'quick',
'quiet',
'quit',
'quote',
'race',
'radio',
'rail',
'rain',
'raise',
'range',
'rare',
'rat',
'rather',
'ratio',
'raw',
're',
'reach',
'react',
'read',
'readily',
'ready',
'real',
'realistic',
'realiz',
'reason',
'receive',
'recent',
'reception',
'recipe',
'recognition',
'recogniz',
'recommend',
'record',
'recover',
'red',
'reduce',
'refer',
'reference',
'reflect',
'refrigerator',
'refuse',
'region',
'register',
'regret',
'regular',
'rel',
'relat',
'relationship',
'relat',
'relax',
'release',
'relevant',
'relief',
'relieve',
'remain',
'remark',
'remember',
'remind',
'remote',
'remov',
'rent',
'repair',
'repeat',
'replace',
'rep',
'report',
'represent',
'representat',
'republic',
'reput',
'request',
'require',
'research',
'reserve',
'resident',
'resist',
'resolut',
'resolve',
'resort',
'resource',
'respect',
'respond',
'response',
'responsibility',
'responsible',
'rest',
'restaurant',
'result',
'retain',
'retire',
'return',
'reveal',
'revenue',
'review',
'revision',
'revolution',
'reward',
'rice',
'rich',
'rid',
'ride',
'right',
'rip',
'rise',
'risk',
'river',
'road',
'rock',
'role',
'roll',
'roof',
'room',
'rope',
'rough',
'round',
'routine',
'row',
'royal',
'rub',
'ruin',
'rule',
'run',
'rush',
'sad',
'safe',
'safety',
'sail',
'salad',
'salary',
'sale',
'salt',
'same',
'sample',
'sand',
'sandwich',
'satisfaction',
'save',
'savings',
'say',
'scale',
'scared',
'scene',
'schedule',
'scheme',
'school',
'science',
'score',
'scratch',
'screen',
'screw',
'script',
'sea',
'search',
'season',
'seat',
'second',
'secret',
'secretary',
'section',
'sector',
'secur',
'sec',
'see',
'seek',
'seem',
'select',
'self',
'sell',
'send',
'senior',
'sense',
'sensitive',
'sentence',
'separ',
'series',
'serious',
'serve',
'service',
'session',
'set',
'setting',
'settl',
'several',
'severe',
'sex',
'sexual',
'shak',
'shall',
'shame',
'shape',
'share',
'sharp',
'she',
'shelter',
'shift',
'shine',
'ship',
'shirt',
'shit',
'shock',
'shoe',
'shoot',
'shop',
'shopp',
'short',
'shot',
'should',
'shoulder',
'show',
'shower',
'shut',
'sick',
'side',
'sign',
'signal',
'signature',
'significance',
'significant',
'sil',
'silver',
'similar',
'simp',
'simple',
'since',
'singer',
'single',
'sink',
'sir',
'sister',
'sit',
'site',
'situ',
'size',
'skill',
'skin',
'skirt',
'sky',
'sleep',
'slice',
'slide',
'slight',
'slip',
'slow',
'small',
'smart',
'smell',
'smile',
'smoke',
'smooth',
'snow',
'so',
'society',
'sock',
'soft',
'software',
'soil',
'solid',
'solut',
'solve',
'some',
'somebody',
'somehow',
'someone',
'something',
'sometimes',
'somewhat',
'somewhere',
'son',
'song',
'soon',
'sorry',
'sort',
'sound',
'soup',
'source',
'south',
'southern',
'space',
'spare',
'speak',
'speaker',
'special',
'specialist',
'specific',
'specify',
'speech',
'speed',
'spell',
'spend',
'spirit',
'spiritual',
'spite',
'split',
'sport',
'spot',
'spr',
'spray',
'spread',
'square',
'st',
'staff',
'stag',
'stand',
'standard',
'star',
'start',
'stat',
'state',
'station',
'status',
'stay',
'steak',
'steal',
'step',
'stick',
'still',
'stock',
'stomach',
'stood',
'stop',
'storage',
'store',
'storm',
'story',
'str',
'straight',
'strain',
'strange',
'stranger',
'strategy',
'street',
'strength',
'stress',
'stretch',
'strict',
'strike',
'strip',
'stroke',
'strong',
'struct',
'struggl',
'student',
'studio',
'study',
'stuff',
'stupid',
'style',
'subject',
'submit',
'substance',
'substantial',
'succeed',
'success',
'successful',
'such',
'suck',
'sucks',
'sudden',
'suffer',
'sufficient',
'sugar',
'suggest',
'suit',
'summer',
'sun',
'super',
'supermarket',
'supp',
'support',
'suppose',
'sure',
'surgery',
'surpris',
'surround',
'survey',
'survive',
'suspect',
'suspicious',
'sw',
'sweet',
'swim',
'swimm',
'switch',
'sympathy',
'system',
'tackle',
'take',
'tale',
'talk',
'tall',
'tank',
'tap',
'target',
'task',
'taste',
'tax',
'tea',
'teach',
'teacher',
'team',
'tear',
'technical',
'technology',
'telephone',
'televis',
'tell',
'temperat',
'temporary',
'tend',
'tennis',
'tens',
'term',
'terrib',
'terrible',
'test',
'text',
'th',
'than',
'thank',
'thanks',
'that',
'the',
'their',
'them',
'theme',
'themselves',
'then',
'theory',
'there',
'therefore',
'these',
'they',
'thick',
'thin',
'think',
'this',
'those',
'though',
'thought',
'three',
'throat',
'through',
'throughout',
'throw',
'thus',
'ticket',
'tie',
'tight',
'till',
'time',
'tiny',
'tip',
'tired',
'title',
'to',
'today',
'toe',
'together',
'tomorrow',
'tone',
'tongue',
'tonight',
'too',
'tool',
'tooth',
'top',
'topic',
'total',
'touch',
'tough',
'tour',
'towards',
'towel',
'tower',
'town',
'track',
'trade',
'tradition',
'traffic',
'train',
'trainer',
'transit',
'translat',
'transport',
'trash',
'travel',
'treat',
'tree',
'trick',
'trip',
'troubl',
'tru',
'truck',
'true',
'trust',
'truth',
'try',
'tune',
'turn',
'twice',
'twist',
'two',
'type',
'typical',
'ugly',
'ultimate',
'un',
'uncle',
'under',
'understand',
'unfair',
'unfortunate',
'unhappy',
'union',
'unique',
'unit',
'united',
'univers',
'unless',
'unlike',
'until',
'unusual',
'up',
'upon',
'upper',
'upset',
'upstairs',
'us',
'use',
'used',
'useful',
'user',
'usual',
'vac',
'vagina',
'valu',
'value',
'vari',
'variety',
'various',
'vary',
'vast',
'vegetable',
'vehicle',
'vers',
'very',
'vessel',
'video',
'view',
'village',
'virtual',
'virus',
'visible',
'visit',
'visual',
'voice',
'volume',
'wait',
'wak',
'walk',
'wall',
'want',
'war',
'warm',
'warn',
'was',
'wash',
'waste',
'watch',
'water',
'wave',
'way',
'we',
'weak',
'weakness',
'wealth',
'wear',
'weather',
'web',
'wedd',
'week',
'weekend',
'weigh',
'weight',
'weird',
'welcome',
'well',
'were',
'west',
'western',
'wet',
'what',
'whatever',
'wheel',
'when',
'whenever',
'where',
'whereas',
'whether',
'which',
'while',
'white',
'who',
'whoever',
'whole',
'whose',
'why',
'wide',
'wife',
'wild',
'will',
'win',
'wind',
'window',
'wine',
'winner',
'winter',
'wise',
'wish',
'with',
'within',
'without',
'witness',
'woman',
'wonder',
'wonderful',
'wood',
'wooden',
'word',
'work',
'worker',
'world',
'worried',
'worry',
'worth',
'would',
'wrap',
'writ',
'writer',
'written',
'wrong',
'yard',
'yeah',
'year',
'yellow',
'yes',
'yesterday',
'yet',
'you',
'young',
'your',
'yours',
'yourself',
'youth',
'zone']

# not used yet
# can this be used instead of having a bunch of ifs-thens?
# probably but i don't have the brains for it atm
wordparts=[
    'ation',
    'ion',
    'ing',
    '‰ing', #‰ means "duplicate the last letter"
    'ism',
    'ist',
    'ally',
    'ly',
    'the',
    'for',
    'are', # ara ara
    'ere', # ara ara
    'with',
    'get',
    'but',
    'who'
    'ter',
    'ver',
    'ate',
    'al',
    'e']
  
smalletters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']+smalletters

import string

words=smalletters+wordlist

def aaaa():
    for c in range(65,91):
        for cc in range(65,91):
            print(chr(c),chr(cc),sep='',end='\n')
        for cc in range(97,123):
            print(chr(c),chr(cc),sep='',end='\n')
    for c in range(97,123):
        for cc in range(65,91):
            print(chr(c),chr(cc),sep='',end='\n')
        for cc in range(97,123):
            print(chr(c),chr(cc),sep='',end='\n')

def num_to_cpl(num):
    num2 = num // 52
    num3 = num % 52
    #print(letters[num2],letters[num3],sep='')
    return ""+letters[num2]+letters[num3]
    
def cpl_to_num(cpl):
    let1 = cpl[0]
    let2 = cpl[1]
    num1 = letters.index(let1)
    num2 = letters.index(let2)
    num3 = (num1*52)+num2
    #print(num3)
    return num3

def shrinkword(wrd):
    wrdo=wrd
    teststr=""
    prestring=""
    sufstring=""
    # catch common suffixes
    # there can be a number of similar rules, and they can be compacted
    if (wrd.endswith("ing")):
        if (len(wrd)>4 and wrd[-4]==wrd[-5] and wrd[-4]!='l'): # swimming, fanning
            wrd=wrd[:-4]
            sufstring="zB" #zB is (last letter)+ing 
        else:    
            wrd=wrd[:-3]
            sufstring="zA" #zA is ing plain

    if (wrd.endswith("est")):
        if (len(wrd)>4 and wrd[-4]==wrd[-5] and wrd[-4]!='l'): # biggest, derpiest
            wrd=wrd[:-4]
            sufstring="zH" #zB is (last letter)+est 
        else:    
            wrd=wrd[:-3]
            sufstring="zI" #zA is est plain
    # there can be a number of similar rules, and they can be compacted
    if (wrd.endswith("ally")):
            wrd=wrd[:-4]
            sufstring="zL"            
    # there can be a number of similar rules, and they can be compacted
    if (wrd.endswith("ly")):
            wrd=wrd[:-2]
            sufstring="zC"
    # there can be a number of similar rules, and they can be compacted
    if (wrd.endswith("ation")):
            wrd=wrd[:-5]
            sufstring="zD" 
    # there can be a number of similar rules, and they can be compacted
    if (wrd.endswith("ion")):
            wrd=wrd[:-3]
            sufstring="zE" 
    # there can be a number of similar rules, and they can be compacted
    if (wrd.endswith("ist")):
            wrd=wrd[:-3]
            sufstring="zF" 
    # there can be a number of similar rules, and they can be compacted
    if (wrd.endswith("ism")):
            wrd=wrd[:-3]
            sufstring="zG"
    # there can be a number of similar rules, and they can be compacted
    if (wrd.endswith("an")):
            wrd=wrd[:-2]
            sufstring="zJ"            
    # there can be a number of similar rules, and they can be compacted
    if (wrd.endswith("ate")):
            wrd=wrd[:-3]
            sufstring="zN"            
    # there can be a number of similar rules, and they can be compacted
    if (wrd.endswith("ment")):
            wrd=wrd[:-4]
            sufstring="zO"            
    # there can be a number of similar rules, and they can be compacted
    if (wrd.endswith("ed")):
            wrd=wrd[:-2]
            sufstring="zM"            
    # there can be a number of similar rules, and they can be compacted
    if (wrd.endswith("able")):
            wrd=wrd[:-4]
            sufstring="zP"            
    # there can be a number of similar rules, and they can be compacted
    if (wrd.endswith("ity")):
            wrd=wrd[:-3]
            sufstring="zQ"            
    # there can be a number of similar rules, and they can be compacted
    if (wrd.endswith("n't")):
            wrd=wrd[:-3]
            sufstring="zR"            
    # there can be a number of similar rules, and they can be compacted
    if (wrd.endswith("ure")):
            wrd=wrd[:-3]
            sufstring="zS"            
    # there can be a number of similar rules, and they can be compacted
    if (wrd.endswith("ive")):
            wrd=wrd[:-3]
            sufstring="zT"            
    try:
        teststr=num_to_cpl(words.index(wrd.lower()))
    # intercept exception and try to build using parts of words
    # not awake enough to do more of it rn
    except:
        wrd=wrdo
        if (wrd.endswith("es")):
            wrd=wrd[:-2]
            sufstring="zK"+sufstring
        elif (wrd.endswith("a")): # iterate these?
            wrd=wrd[:-1]
            sufstring="xa"+sufstring
        elif (wrd.endswith("e")):
            wrd=wrd[:-1]
            sufstring="xe"+sufstring
        elif (wrd.endswith("n")):
            wrd=wrd[:-1]
            sufstring="xn"+sufstring
        elif (wrd.endswith("y")):
            wrd=wrd[:-1]
            sufstring="xy"+sufstring
        elif (wrd.endswith("s")):
            wrd=wrd[:-1]
            sufstring="xs"+sufstring
        elif (wrd.endswith("r")):
            wrd=wrd[:-1]
            sufstring="xr"+sufstring
        try:
            teststr=num_to_cpl(words.index(wrd.lower()))
    # intercept exception and transmit as-is using literal
        except:
            wrd=wrdo
            ll=len(wrd)-1
            prestring="y"+smalletters[ll]
            sufstring=""
            if (ll % 2 == 0): # temp fix for it only working on even letterd words
                wrdo=wrdo+" " # temp fix for it only working on even letterd words
            teststr=wrdo
    return prestring+teststr+sufstring

def expword(wrd): # ‰ means backspace
    if (wrd=="zI"):
        return "‰est"
    if (wrd=="zH"):
        return "‰@est"
    if (wrd=="zA"):
        return "‰ing"
    if (wrd=="zB"):
        return "‰@ing"
    if (wrd=="zC"):
        return "‰ly"
    if (wrd=="zE"):
        return "‰ion"
    if (wrd=="zD"):
        return "‰ation"
    if (wrd=="zF"):
        return "‰ist"
    if (wrd=="zG"):
        return "‰ism"
    if (wrd=="zJ"):
        return "‰an"
    if (wrd=="zK"):
        return "‰es"
    if (wrd=="zN"):
        return "‰ate"
    if (wrd=="zM"):
        return "‰ed"
    if (wrd=="zL"):
        return "‰ally"
    if (wrd=="zO"):
        return "‰ment"
    if (wrd=="zP"):
        return "‰able"
    if (wrd=="zQ"):
        return "‰ity"
    if (wrd=="zR"):
        return "‰n't"
    if (wrd=="zS"):
        return "‰ure"
    if (wrd=="zT"):
        return "‰ive"
    if (wrd[0]=='x'):
        return "‰"+wrd[1]
    if (wrd[0]=='y'):
        return "‡"+wrd[1]
    return words[cpl_to_num(wrd)]

def shrinkphrase(sentence):
    sentence = sentence.replace(",","")
    sentence = sentence.replace(":","")
    sentence = sentence.replace(".","")
    sentence = sentence.replace(";","")
    sentence = sentence.replace("-"," ")
    # just strip punctuation for now. logically rn puncts and numbers could pass thru
    # i don't have the brains to write a pass thru though rn
    wordlist = sentence.split()
    strung=""
    for wrd in wordlist:
        strung+=shrinkword(wrd)
    strung = strung.replace("xyzC","xy") #lyly
    print (len(sentence),len(strung))
    return strung

def expphrase(shrunk):
    out = [(shrunk[i:i+2]) for i in range(0, len(shrunk), 2)]
    expy=""
    passthru=0
    for wrd in out:
        if (passthru<1):
           ww = expword(wrd)
           if (ww[0]=='‡'):
              passthru=smalletters.index(ww[1])+1
              #print (passthru)
           else:
              expy+=ww+" "
        else: # only works with an even number of letters right now, fixme
            expy+=wrd
            passthru-=2
            if (passthru==0):
               expy+=" "

    expy = expy.replace(" ‰","")
    expy = expy.replace("istist","ist") # intersecting rules; fix / prevent waste
    expy = expy.replace("ationation","ation") # intersecting rules; fix / prevent waste
    expy = expy.replace("ateate","ate") # intersecting rules; fix / prevent waste
    return expy
    

print("dict size is",len(wordlist),"max is",52*49)
testphrase="i am surprised that this works online. do you have any food please. there is no sense in fighting if we can talk i have cookies if you would like to have a conversation over cookies the word blabla does not exist"
testcomp=shrinkphrase(testphrase)
testexp=expphrase(testcomp)
print(testphrase)
print(testcomp)
print(testexp)

    