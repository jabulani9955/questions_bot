PGDMP     4                    {         
   example_db    15.1    15.1 #               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                        0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            !           1262    16445 
   example_db    DATABASE     ~   CREATE DATABASE example_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE example_db;
                postgres    false            �            1259    16558    answers    TABLE     �   CREATE TABLE public.answers (
    id integer NOT NULL,
    question_id integer,
    answer character varying(255) NOT NULL,
    created_at timestamp without time zone NOT NULL,
    is_correct boolean DEFAULT false NOT NULL
);
    DROP TABLE public.answers;
       public         heap    postgres    false            �            1259    16557    answers_id_seq    SEQUENCE     �   CREATE SEQUENCE public.answers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.answers_id_seq;
       public          postgres    false    217            "           0    0    answers_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.answers_id_seq OWNED BY public.answers.id;
          public          postgres    false    216            �            1259    16551 	   questions    TABLE     �   CREATE TABLE public.questions (
    id integer NOT NULL,
    question character varying(255) NOT NULL,
    created_at timestamp without time zone NOT NULL
);
    DROP TABLE public.questions;
       public         heap    postgres    false            �            1259    16550    questions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.questions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.questions_id_seq;
       public          postgres    false    215            #           0    0    questions_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.questions_id_seq OWNED BY public.questions.id;
          public          postgres    false    214            �            1259    16627    user_answers    TABLE       CREATE TABLE public.user_answers (
    id integer NOT NULL,
    user_id bigint NOT NULL,
    question_id integer,
    answer_id integer NOT NULL,
    answer_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    is_correct_answer boolean NOT NULL
);
     DROP TABLE public.user_answers;
       public         heap    postgres    false            �            1259    16626    user_answers_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_answers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.user_answers_id_seq;
       public          postgres    false    221            $           0    0    user_answers_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.user_answers_id_seq OWNED BY public.user_answers.id;
          public          postgres    false    220            �            1259    16617    users    TABLE       CREATE TABLE public.users (
    id integer NOT NULL,
    user_id bigint NOT NULL,
    username character varying,
    first_name character varying,
    last_name character varying,
    first_login_time timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false            �            1259    16616    users_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.users_id_seq;
       public          postgres    false    219            %           0    0    users_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;
          public          postgres    false    218            u           2604    16561 
   answers id    DEFAULT     h   ALTER TABLE ONLY public.answers ALTER COLUMN id SET DEFAULT nextval('public.answers_id_seq'::regclass);
 9   ALTER TABLE public.answers ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    216    217            t           2604    16554    questions id    DEFAULT     l   ALTER TABLE ONLY public.questions ALTER COLUMN id SET DEFAULT nextval('public.questions_id_seq'::regclass);
 ;   ALTER TABLE public.questions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            y           2604    16630    user_answers id    DEFAULT     r   ALTER TABLE ONLY public.user_answers ALTER COLUMN id SET DEFAULT nextval('public.user_answers_id_seq'::regclass);
 >   ALTER TABLE public.user_answers ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    221    221            w           2604    16620    users id    DEFAULT     d   ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);
 7   ALTER TABLE public.users ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    218    219                      0    16558    answers 
   TABLE DATA                 public          postgres    false    217   �%                 0    16551 	   questions 
   TABLE DATA                 public          postgres    false    215   �'                 0    16627    user_answers 
   TABLE DATA                 public          postgres    false    221   J)                 0    16617    users 
   TABLE DATA                 public          postgres    false    219   �,       &           0    0    answers_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.answers_id_seq', 48, true);
          public          postgres    false    216            '           0    0    questions_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.questions_id_seq', 12, true);
          public          postgres    false    214            (           0    0    user_answers_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.user_answers_id_seq', 53, true);
          public          postgres    false    220            )           0    0    users_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.users_id_seq', 3, true);
          public          postgres    false    218            ~           2606    16564    answers answers_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.answers
    ADD CONSTRAINT answers_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.answers DROP CONSTRAINT answers_pkey;
       public            postgres    false    217            |           2606    16556    questions questions_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.questions
    ADD CONSTRAINT questions_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.questions DROP CONSTRAINT questions_pkey;
       public            postgres    false    215            �           2606    16633    user_answers user_answers_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.user_answers
    ADD CONSTRAINT user_answers_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.user_answers DROP CONSTRAINT user_answers_pkey;
       public            postgres    false    221            �           2606    16625    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    219            �           2606    16565     answers answers_question_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.answers
    ADD CONSTRAINT answers_question_id_fkey FOREIGN KEY (question_id) REFERENCES public.questions(id);
 J   ALTER TABLE ONLY public.answers DROP CONSTRAINT answers_question_id_fkey;
       public          postgres    false    215    3196    217            �           2606    16639 (   user_answers user_answers_answer_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_answers
    ADD CONSTRAINT user_answers_answer_id_fkey FOREIGN KEY (answer_id) REFERENCES public.answers(id);
 R   ALTER TABLE ONLY public.user_answers DROP CONSTRAINT user_answers_answer_id_fkey;
       public          postgres    false    221    217    3198            �           2606    16634 *   user_answers user_answers_question_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_answers
    ADD CONSTRAINT user_answers_question_id_fkey FOREIGN KEY (question_id) REFERENCES public.questions(id);
 T   ALTER TABLE ONLY public.user_answers DROP CONSTRAINT user_answers_question_id_fkey;
       public          postgres    false    3196    215    221               �  x��׻N�@�>O1�A2�v��@�E7%@�ڃv$�a�-H(���6 ����0�F3#ڤ��|�4��s�Hn�w��[����A�{<���<bB�)��0g2�i�->̊K"�h��.�\�e7J�`Q6MvW��;d�w	��&\:�xAu��g����0���Z�o΅����M/TZe@i��l�c���� UYKe��RBK���1.����ӡY.\J�PV��1�ڴs��F���)5���찄	�Ki�F�Y��d��J+��xJ�}��F�Υ��Rn*��lw�!���Qw��^Շ��O�<Ȯкz����zGլ�I��׉S*���t���"z�k���A��\+T�8�Ȟ����^$�Op�ִ�ǯ���_���5�7�Q�w�.uO�"k`î��j Iԋ�FO(��[5�q�Ч�NW�YU��;��>���-�m������T*�yF1�         i  x����NA�{�b: ��Q,�&$A-�z�r�y{����)Ġ������(r���9��P��\1������f�fm��Fk���s��y��r_@�m��Z ;t�t�GL��`kg�ք�Q��a�IpȎ6\�<�'�2�v6��0�f�X6��Vղ�f�d�[�Y��72�2�KO���|�Tx�ः�
霥 UY�:㚈��#6�|v5�~���Nʢ��C�wR$��&�K�?�HpJB�np�	���J��v�1�u�q
�+�����ϩ�̐�鷐�+�����/Pu~�BO���>�H��5���L��5�V��Ԓ�I�%�1Ě���;�м�m�'���7jw         c  x�řMkG���s�rS��Փ�>����Q���J��zV��hk��=�.���5����ܼ���������?���r�O��ۯ���������0��.�?N�߾N_η�/?�>���ӧ�o������_^���Ϸ��x= 0Ւ�r��  ~��q �F�K�Y_\��ë߮n~)&-0��u15����~9�zN^s�.gNVj�u���l��崄�P�8u�9Qw9kb@������@��q�,N�rb�
d5���l�A�rR�հh؁�hW���3T�:���3�&N�V��O��Ma�>��BQ�O$�w�צ�IN����dN�";�)�s=�Μ%��I}�go&M�>;� q�i�9�i��-O(V$4/@{��,�� ��㴩,@{�t�d(��Jo�ڤu���0̺/M3��C	)L����A��RU�P�����T\B��@�mrP�Tŏ4��_�Mʘ�a\�����;�����{I��^Z�S��ƙ�"������H������Ϡ>��,�v3����H	J�8�g�3�% "	;Q��J(z��&N��J��D�G��>TI��bth��TA�2Вژ����Tz��H1�8P]�r��
 Όr�1�O��v̀a։ˎi~��T�2��f��i�]NO!\���8'l�yT��	9ngk��DN�CjtRJHTr\��杒tA9����͘���>甄X �0�杒u15��\�ށ��A��S[�H�՟G�%����0���� ��Y��rN A�\V��Zb��A乬4��1n?"۬Tz��-���fRX�R���	܉B�>)>�?礒�m�Ê���6���h�t9��IyN�-/���ϫ�����         �   x���Ao�@��;�bnh���V�����`R�+Y��L���@��^д�^���\���j�QC^�k��w�?����&�0f����/>�]�hg��qv���㣝����,+�� E(	�d. �6���i�u8�w����0Q"ͤ���2ER�D�y8}	�kI &�>⨭�f�Og�;r�������,ƌ�5)�����mh(     