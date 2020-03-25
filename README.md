# push-biometric-legoerp
Python Script to poll for biometric logs and push to LegoERP via API.

## Instructions to run this script
1. Install python3.6+ and git (python versions below 3.6 is **NOT** supported)
2. Clone this repository using `git clone https://github.com/mainul94/push-biometric-legoerp`
3. Setup dependencies using `cd push-biometric-legoerp && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
4. Setup `local_config.py` by making a copy of and renaming `local_config.py.template` file. ([Learn More](#Note-on-setting-up-local-config))
5. Run this script using `python3 push_to_legoerp.py`

## Installing as a windows service
1. Install pywin32 using `pip install pywin32`
2. Got to this repository's Directory
3. Install the windows service using `python push_biometric_windows_service.py install`
4. Done

#### Update the installed windows service
> python push_biometric_windows_service.py update

#### Stop the windows service
> net stop LegoERPBiometricPushService

#### To see the status of the service
> mmc Services.msc

### Note on setting up local config
- You need to make a copy of `local_config.py.template` file and rename it to `local_config.py`
- Please fill in the relevant sections in this file as per the comments in it.
- Below are the delineation of the keys contained in `local_config.py`:
  - LegoERP connection configs:
    - `LEGOERP_API_KEY`: The API Key of the LegoERP User
    - `LEGOERP_API_SECRET`: The API Secret of the LegoERP User
      > Please refer to [this link](https://frappe.io/docs/user/en/guides/integration/how_to_set_up_token_based_auth#generate-a-token) to learn how to generate API key and secret for a user in LegoERP. 

      > The LegoERP User who's API key and secret is used, needs to have at least the following permissions: 

      > 1. Create Permissions for 'Employee Checkin' DocType.

      > 2. Write Permissions for 'Shift Type' DocType.
    - `LEGOERP_URL`: The web address at which you would access your LegoERP. eg:`'https://yourcompany.legoerp.com'`, `'https://erp.yourcompany.com'`
  - This script's operational configs:
    - `PULL_FREQUENCY`: The time in minutes after which a pull for punches from the biometric device and push to LegoERP is attempted again.
    - `LOGS_DIRECTORY`: The Directory in which the logs related to this script's whereabouts are stored.
      > Hint: For most cases you can leave the above two keys unchanged. 
    - `IMPORT_START_DATE`: The date after which the punches are pushed to LegoERP. Expected Format: `YYYYMMDD`.
      > For some cases you would have a lot of old punches in the biometric device. But, you would want to only import punches after certain date. You could set this key appropriately. Also, you can leave this as `None` if this case does not apply to you.
> TODO: fill this section with more info to help Non-Technical Individuals.

#### Other TODO:
 - Write a setup/auto-install script and ask questions to fill-in/update the `local_config.py` file.
 - Write a dev note on how stuff works in the `push_to_legoerp.py` script?