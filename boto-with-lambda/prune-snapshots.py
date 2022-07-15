import boto3

def lambda_handler(event, context):
    
    # gets account id
    account_id = boto3.client('sts').get_caller_identity().get('Account')
    
    ec2 = boto3.client('ec2')
    
    # grabs regions
    regions = [region['RegionName']
                for region in ec2.describe_regions()['Regions']]
    
    # iterates through regions 
    for region in regions:
        print('Region:', region)
        ec2 = boto3.client('ec2', region_name = region)
        
        # desribe snapshots
        response = ec2.describe_snapshots(OwnerIds=[account_id])
        snapshots = response['Snapshots']
        
        # sort snapshots by date ascending
        snapshots.sort(key=lambda x: x['StartTime'])
        
        # remove the snapshots we want to keep (3 most recent)
        snapshots = snapshots[:-3]
        
        # iterate through snapshots and delete them by id
        for snap in snapshots:
            id = snap['SnapshotId']
            try:
                print('Deleting snapshot:', id)
                ec2.delete_snapshot(SnapshotId=id)
            # if snapshot is being used by an ebs volume, catch the exception
            # and contiune the loop
            except Exception as e:
                if 'InvalidSnapshot.InUse' in e.message:
                    print('Snapshot {} in use, skipping'.format(id))
                    continue