U
    �;`'  �                
   @   s�   d dl Z d dlZd dlZzVd dlmZ d dlmZ eZej	Z
ejZejZejZdd� Zdd� Zdd	� Ze�  W n4 ek
r� Z zed
� e�d� W 5 dZ[X Y nX dS )�    N)�Fore)�CreditCardCheckerc                   C   s   t t� dt� dt� d�� d S )Nzp	
|                               |
|===============================|
|-------------------------------|
~~~~~[+]zBy: Anikin Lukea%   [+]~~~~~~
	 Valid/Live CC-Generator

[1] ===== Amazon Prime Video CC
[2] ===== HBO max CC
[3] ===== Netflix CC
[4] ===== CC-checker(CreditCard-Checker)
[0] ===== Exit
[000] === Shutdown... 

|-------------------------------|
|===============================|
|                               |)�print�y�r� r   r   �card.py�menu   s    �r	   c                 C   s   d}dddddddg}d	d
ddddddddddg}t d� ttd��}d}||kr�t�|�}d�|�}t�|�}d�|�}	tjt|�dd�}
d�|
�}tjt|�dd�}| d�|� }t|��� }|dkrJ|d7 }t |� d|	� d|� d|� �� t	�
d� qJd S ) NZ
1234567890Z2022Z2023Z2024Z2025Z2026Z2027Z2028Z01Z02Z03Z04Z05Z06Z07Z08Z09Z10Z11Z12zHow many cc to generatezEnter any Value: r   � �   )�k�   T�   �|皙�����?)r   �int�input�random�choices�join�list�cccZvalid�time�sleep)�binZnumbersZyyyyZmm�uiZamountZy_rZy_jZm_rZm_jZcvv_rZcvv_jZcc_rZcc_jZcheckr   r   r   �	generator"   s(    




r   c                  C   s�   t �  tt� dt� d�� tt� dt� d��} | dkrDd}t|� q| dkrZd}t|� q| d	krpd
}t|� q| dkr�td�D ]}tt� d�� t�	d� q�q| dkr�t
�d� q| dkr�q�qt
�| � qd S )Nu
   ┌──(u   Anikin㉿Luke)-[~/Carding]u
   └─>->>� �1Z45101560210�2Z52215801230�3Z52215800230�4�
   zCOMMING SOON!!r   Z000zsudo shutdown now�0)r	   r   r   r   r   �gr   �ranger   r   �os�system)r   r   �ir   r   r   �main<   s*    


r)   z|Some python modules are/is not installed!
 Enter root password to grant us permission to auto install this required modules!zAsudo pip3 install colorama; sudo pip3 install credit_card_checker)r   r   r&   Zcoloramar   Zcredit_card_checkerr   r   �fZREDr   ZYELLOWr   ZGREENr$   ZBLUE�br	   r   r)   �ImportErrorZimerrr   r'   r   r   r   r   �<module>   s   !
